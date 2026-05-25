---
type: item
source-type: "Remaster"
level: "12"
traits: ["[[Coda]]", "[[Invested]]", "[[Magical]]", "[[Staff]]"]
price: "{'gp': 2000}"
usage: "worncollar"
bulk: "—"
source: "Pathfinder #205: Singer, Stalker, Skinsaw Man"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This collar is a silken cord from which hangs a small silver amulet that bears the likeness of a woman with her hand at her throat. A *gasping lament* is a powerful coda instrument that's worn rather than held. While you sing, you gain a +2 item bonus to Intimidation checks to [[Demoralize]] and to Performance checks.

**Activate** Cast a Spell

**Effect** You expend a number of charges from the collar to cast a spell from its list.

- **Cantrip** [[Message]]
- **1st** [[Charm]], [[Command]]
- **2nd** [[Sonata Span]], [[Ventriloquism]]
- **3rd** [[Enthrall]], [[Shatter]]
- **4th** [[Honeyed Words]], [[Infectious Melody]]
- **5th** [[Command]], [[Concordant Choir]]

**Craft Requirements** Supply one casting of all listed levels of all listed spells.

**Source:** `= this.source` (`= this.source-type`)
