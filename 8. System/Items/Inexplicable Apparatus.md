---
type: item
source-type: "Remaster"
level: "18"
traits: ["[[Invested]]", "[[Magical]]"]
price: "{'gp': 19000}"
usage: "worngarment"
bulk: "2"
source: "Pathfinder GM Core"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This strange and intricate harness fits snugly to the torso. Once you invest the apparatus, numerous artificial limbs with various tools, clamps, and lenses whirl into action, following your mental commands effortlessly.

When using this apparatus, you gain a +3 item bonus to Crafting checks to Craft, Earn Income, and Repair, and you reduce the minimum time required to Craft an item to 1 day.

If you succeed at your Crafting check and spend more downtime to continue work on the item after the minimum number of days, each day you spend reduces the remaining raw material cost by an amount based on your level + 1 and your proficiency rank in Crafting; on a critical success, each day reduces the remaining raw material cost by an amount based on your level + 2 and your proficiency rank. If you are 20th level, on a critical success your progress is 50 gp, 100 gp, 200 gp, or 350 gp for trained, expert, master, or legendary proficiency, respectively.

**Activate—Inexplicable Patch** `pf2:2` (concentrate, manipulate)

**Frequency** once per day

**Effect** You command the apparatus to magically jury-rig an item you hold or that's within 5 feet of you. The item is repaired, as a 3rd-rank [[Mending]] spell. This lasts for 10 minutes, after which the item returns to its previous state of disrepair unless you've Repaired it before then.

**Source:** `= this.source` (`= this.source-type`)
