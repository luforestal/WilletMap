/**
 * School Configuration Loader
 * Loads school metadata and provides utilities for multi-school support
 */

// Use relative paths that work both locally and on GitHub Pages
const BASE_PATH = import.meta.env.BASE_URL || '/'

/**
 * Parse CSV text into array of objects
 */
function parseCSV(csvText) {
  const lines = csvText.trim().split('\n')
  const headers = parseCSVLine(lines[0])
  
  return lines.slice(1).map(line => {
    const values = parseCSVLine(line)
    const obj = {}
    headers.forEach((header, i) => {
      obj[header] = values[i] || ''
    })
    return obj
  })
}

/**
 * Parse a single CSV line handling quoted values
 */
function parseCSVLine(line) {
  const values = []
  let current = ''
  let inQuotes = false
  
  for (let i = 0; i < line.length; i++) {
    const char = line[i]
    
    if (char === '"') {
      inQuotes = !inQuotes
    } else if (char === ',' && !inQuotes) {
      values.push(current.trim())
      current = ''
    } else {
      current += char
    }
  }
  values.push(current.trim())
  
  return values
}

/**
 * Load schools configuration from CSV
 */
export async function loadSchools() {
  try {
    const response = await fetch(`${BASE_PATH}schools.csv`)
    if (!response.ok) {
      throw new Error(`Failed to load schools: ${response.statusText}`)
    }
    
    const csvText = await response.text()
    const schools = parseCSV(csvText)
    
    return schools.map(school => ({
      id: school.id,
      school_name: school.school_name,
      logo: school.logo ? `${BASE_PATH}${school.logo}` : `${BASE_PATH}logos/${school.id}.png`,
      address: school.address,
      data_file: school.data_file || `trees/${school.id}.csv`,
      boundary_file: school.boundary_file || `boundaries/${school.id}.geojson`,
      photos_folder: school.photos_folder || `photos/${school.id}`,
      dataUrl: `${BASE_PATH}${school.data_file || `trees/${school.id}.csv`}`,
      boundaryUrl: `${BASE_PATH}${school.boundary_file || `boundaries/${school.id}.geojson`}`,
      photosUrl: `${BASE_PATH}${school.photos_folder || `photos/${school.id}`}`
    }))
  } catch (error) {
    console.error('Error loading schools:', error)
    throw error
  }
}

/**
 * Get school ID from URL parameter
 * Format: ?school=wildav
 */
export function getSchoolIdFromURL() {
  const params = new URLSearchParams(window.location.search)
  return params.get('school') || 'wildav' // Default to wildav
}

/**
 * Get school configuration by ID
 */
export async function getSchoolConfig(schoolId) {
  const schools = await loadSchools()
  const school = schools.find(s => s.id === schoolId)
  
  if (!school) {
    throw new Error(`School not found: ${schoolId}`)
  }
  
  return school
}

/**
 * Load boundary data for a school
 */
export async function loadSchoolBoundary(boundaryUrl) {
  try {
    const response = await fetch(boundaryUrl)
    if (!response.ok) {
      console.warn(`No boundary file found: ${boundaryUrl}`)
      return null
    }
    return await response.json()
  } catch (error) {
    console.warn(`Error loading boundary: ${boundaryUrl}`, error)
    return null
  }
}
