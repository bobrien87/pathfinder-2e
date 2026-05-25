---
type: item
source-type: "Remaster"
level: "14"
traits: ["[[Consumable]]", "[[Magical]]", "[[Mythic]]", "[[Structure]]"]
price: "{'gp': 900}"
usage: "other"
bulk: "—"
source: "Pathfinder #220: Crypt of Runes"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Azeradni, third runelord of sloth, is said to have used solid-gold seeds to sow her legendary, self-sustaining gardens.

**Activate—Sow Garden** 1 minute (concentrate, manipulate)

**Effect** You place the seed on the ground in an adjacent space. Over the next minute, the seed's magic creates an elegant garden in a 40-foot-square area that includes the space where you placed the seed. As the garden grows, you choose to fill each 10-foot-square space with lawns (normal terrain), flower beds (difficult terrain), or hedgerows. Hedgerows are filled with 10-foot-tall hedges that grant standard cover and are greater difficult terrain. The garden withers after 24 hours.

If you place the seed on natural earth and spend 1 Mythic Point during the activation, the garden establishes itself in the area and grows indefinitely, so long as the plants receive adequate sunlight and rain. While it remains, the garden remains free of weeds and pests, with the plants never growing beyond their bounds, as if tended by a master gardener.

**Source:** `= this.source` (`= this.source-type`)
