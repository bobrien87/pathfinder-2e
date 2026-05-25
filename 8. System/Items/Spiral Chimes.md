---
type: item
source-type: "Remaster"
level: "13"
traits: ["[[Air]]", "[[Magical]]"]
price: "{'gp': 2500}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Rage of Elements"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

*Spiral chimes* are a set of small metal bells decorated with spiraling designs that hang on thin wires from a carved statue of a storm cloud or air elemental. Each bell in the *spiral chimes* rings at a different tone, and when caught in the turbulent winds of a storm, the bells combine to create deep, full songs.

A set of *spiral chimes* is a planar key for [[Interplanar Teleport]] and similar magic. When the chimes are used this way, you're more likely to arrive where you intend to be, appearing 1d6×25 miles from your intended destination instead of 1d10×25 miles away.

**Activate—Forecast Chime** 10 minutes (manipulate, prediction)

**Effect** You let the *spiral chimes* play in the wind, interpreting the music to predict the weather at your location for the next 24 hours. You receive advanced warning of the temperature, humidity, storms, natural disasters (such as tornadoes, floods, or volcanic eruptions), and other weather conditions that naturally arise. The information you gain through the *spiral chimes* doesn't take magical occurrences that might change the weather into account.

**Activate—Revealing Chime** `pf2:1` (manipulate, sonic)

**Frequency** once per day

**Effect** You ring the chimes, blanketing everything in a @Template[burst|distance:30] within 120 feet in visible, reverberating sound. This can negate invisibility, making creatures [[Concealed]] instead of [[Invisible]]. The duration and other effects depend on the result of each creature's attempt at a DC 30 [[Reflex]] save.
- **Critical Success** The target is unaffected.
- **Success** The target's invisibility is negated for 2 rounds.
- **Failure** The target is [[Deafened]] for 1 minute, and its invisibility is negated for 1 minute.
- **Critical Failure** The target is deafened for 10 minutes, and its invisibility is negated for 10 minutes.

**Source:** `= this.source` (`= this.source-type`)
