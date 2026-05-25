---
type: item
source-type: "Remaster"
level: "2"
traits: ["[[Consumable]]", "[[Magical]]"]
price: "{'gp': 7}"
bulk: "—"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** A (manipulate)

Creation of these arrows was inspired by an encounter with a horned archon scout who sought to peacefully restrain their foes. When an activated *antler arrow* hits a target, bone antlers extend to pin it down. The target must succeed at a DC 16 [[Reflex]] save or become stuck to the surface, taking the critical specialization effects of a bow.

If the hit with the *antler arrow* is a critical hit and you have access to the bow critical specialization effect, the DC of the Athletics check increases to 15.

**Source:** `= this.source` (`= this.source-type`)
