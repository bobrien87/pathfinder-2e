---
type: item
source-type: "Remaster"
level: "6"
traits: ["[[Darkness]]", "[[Grimoire]]", "[[Magical]]", "[[Shadow]]"]
price: "{'gp': 200}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This grim collection of spreadsheets is used both by undertakers who occasionally need to avoid the notice of their more restless clients, and by industrious necromancers looking to avoid catching the notice of cemetery guards and vigilant undertakers.

**Activate** `pf2:f` (concentrate)

**Frequency** once per day

**Effect** If your next action is to cast a shadow or void spell, the spell's casting is accompanied by a roiling cloud of shadow that spills out around you, creating dim light in a @Template[type:emanation|distance:30] centered on you for the next 3 rounds. This has no effect on areas where the lighting level is already darker than dim light.

**Source:** `= this.source` (`= this.source-type`)
