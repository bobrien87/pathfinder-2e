---
type: item
source-type: "Remaster"
level: "1"
price: "{'gp': 1}"
usage: "held-in-one-hand"
bulk: "—"
source: "Pathfinder #201: Pactbreaker"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** `pf2:2` (manipulate)

This device resembles a teapot with a trigger. When filled with cloth fuel (worth 1 cp) and lit, it smolders and gradually fills with smoke for 10 minutes, during which time you can squeeze the trigger to spray smoke.

**Spray Smoke** `pf2:1` (manipulate)

**Frequency** once per minute

**Effect** You expel smoke into an adjacent 5-foot square. All creatures in that area are [[Concealed]], and other creatures are concealed to them. The smoke lasts for 1d4 rounds or until dispersed by strong wind.

**Source:** `= this.source` (`= this.source-type`)
