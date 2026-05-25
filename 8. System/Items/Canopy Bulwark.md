---
type: item
source-type: "Remaster"
level: "8"
traits: ["[[Invested]]", "[[Laminar]]", "[[Magical]]"]
price: "{'gp': 550}"
bulk: "1"
source: "Pathfinder #201: Pactbreaker"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This suit of *+1 assisting leaf weave* is composed entirely of primal-infused leaves bestowed by a dying arboreal. The leaves display the vibrant greens of summer, as if full of life, regardless of the time that has passed since the arboreal gifted them. The armor is constantly drawing in imperceptible amounts of primal energy to help bear its wearer's burdens. You can draw deeply upon the untapped reserves of primal magic within it and infuse yourself with these energies to a limited extent, giving you a burst of quickness.

**Activate** `pf2:2` command, envision

**Frequency** once per day

**Effect** You cast [[Haste]] targeting yourself. In addition to the effects of the spell, visible primal energy surges over the armor for the duration. This has no mechanical impact.

**Craft Requirements** The initial raw materials must include leaves freely given by an arboreal.

**Source:** `= this.source` (`= this.source-type`)
