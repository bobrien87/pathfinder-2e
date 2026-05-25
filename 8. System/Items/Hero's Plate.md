---
type: item
source-type: "Remaster"
level: "10"
traits: ["[[Bulwark]]"]
price: "{'gp': 1000}"
bulk: "4"
source: "Pathfinder #202: Severed at the Root"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Golden images of heroic deeds decorate the black plates of this *+1 resilient full plate*. You gain resistance 5 to mental damage and a +1 status bonus to saves against fear.

**Activate—Personal Legend** `pf2:1` (concentration)

**Frequency** once per day

**Effect** The scenes depicted on your armor shift and change, making room to accommodate your current heroic feats. You cast [[Heroism]] on yourself.

**Source:** `= this.source` (`= this.source-type`)
