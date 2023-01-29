/*************************************************************************//**
 *  @file  N2kDef.h
 *  @brief Type definitions and utility macros used in the NMEA2000 libraries.
 * 
 */
#ifndef _tN2kDef_H_
#define _tN2kDef_H_

#include <stdint.h>

#if !defined(ARDUINO)
extern "C" {
// Current uptime in milliseconds. Must be implemented by application.
extern uint32_t millis();
}
#endif

// Declare PROGMEM macros to nothing on non-AVR targets.
#if !defined(__AVR__) && !defined(ARDUINO)
// ESP8266 provides it's own definition - Do not override it.
#if !defined(ARDUINO_ARCH_ESP8266)
#define PROGMEM
#define pgm_read_byte(var)  *var
#define pgm_read_word(var)  *var
#define pgm_read_dword(var) *var
#endif
#endif

// Definition for the F(str) macro. On Arduinos use what the framework
// provides to utilize the Stream class. On standard AVR8 we declare
// our own helper class which is handled by the N2kStream. On anything
// else we resort to char strings.
#if defined(ARDUINO)
#include <WString.h>
#elif defined(__AVR__)
#include <avr/pgmspace.h>
class __FlashStringHelper;
#define F(str) (reinterpret_cast<const __FlashStringHelper*>(PSTR(str)))
#else
#ifndef F
#define F(str) str
#endif
#endif

#endif
