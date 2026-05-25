---
type: item
source-type: "Remaster"
level: "12"
traits: ["[[Clockwork]]", "[[Magical]]"]
price: "{'gp': 1800}"
usage: "worn"
bulk: "3"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This clockwork traveler's chair has spinnerets and spider legs that allow it to roll up walls, fire web lines to pull you to a location, and obstruct foes with webs. While using the chair, you gain a climb Speed equal to your Speed.

**Activate—Web Swing** `pf2:1` (manipulate)

**Frequency** once per minute

**Effect** The chair shoots a web line at a solid wall, floor, or ceiling up to 60 feet away and then pulls itself and you to that location.

**Activate—Web** `pf2:3` (manipulate)

**Frequency** once per hour

**Effect** You cause the chair to launch an enormous web to hinder your foes, with the effects of a 4th-rank [[Web]] spell.

**Source:** `= this.source` (`= this.source-type`)
