---
type: item
source-type: "Remaster"
level: "9"
traits: ["[[Light]]", "[[Magical]]"]
price: "{'gp': 650}"
usage: "held-in-one-hand"
bulk: "3"
source: "Pathfinder Lost Omens Rival Academies"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

An *inspiring spotlight* consists of a drum-shaped metal housing around several reflective plates. It has the capacity to cast a powerful, narrow beam of light to illuminate important moments or characters on stage. The portable version consists of an 18-inch-diameter lamp on a tripod that can be set up or broken down over the course of 10 minutes. The mounted version is typically 3 feet in diameter and affixed to a bracket above and behind the audience for indoor performances.

**Activate—Light It Up** `pf2:1` (light, manipulate)

**Frequency** once per hour

**Effect** The inspiring spotlight emits a @Template[type:burst|distance:5] of bright magical light within 120 feet. If the burst intersects with an area of magical darkness, the inspiring spotlight attempts to counteract the darkness with a +17 modifier. Creatures within the burst gain a +1 item bonus to saving throws and Charisma-based skill checks. The spotlight remains lit for 1 minute or until you Interact to turn it off. During this time any creature adjacent to the spotlight can move the burst up to 20 feet from the burst's original position with an Interact action.

**Source:** `= this.source` (`= this.source-type`)
