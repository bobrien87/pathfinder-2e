---
type: item
source-type: "Remaster"
level: "10"
traits: ["[[Agile]]", "[[Finesse]]", "[[Versatile s]]"]
price: "{'cp': 0, 'gp': 900, 'pp': 0, 'sp': 0}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Lost Omens Shining Kingdoms"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Access** You're a member of the Lion Blades.

Given only to highly trusted agents by the grand princes back when Lion Blades protected the Primogen Crown, these historic *+1 striking authorized shortswords* allow a Lion Blade wielder to locate resources.

**Activate—Find the Pride** `pf2:3` (arcane, concentrate, manipulate)

**Frequency** once per day

**Effect** You cast [[Locate]] at 5th rank to learn the location of one of the following of your choice: the nearest Lion Blade safe house, shadow school, Lion Blade agent, Lion Blade kith, or a person other than yourself who's in possession of a *lion's call*.

**Activate—Echo the Call** `pf2:r` (arcane, concentrate)

**Frequency** once per day

**Trigger** A creature locates you using another *lion's call*

**Effect** You immediately learn the location and appearance of the triggering creature. You can communicate telepathically with the triggering creature while you remain within 1 mile of each other for the next hour

**Source:** `= this.source` (`= this.source-type`)
