---
type: item
source-type: "Remaster"
level: "11"
traits: ["[[Consumable]]", "[[Illusion]]", "[[Magical]]", "[[Talisman]]"]
price: "{'gp': 275}"
usage: "affixed-to-armor"
bulk: "—"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** `pf2:f` (concentrate)

**Trigger** You roll Stealth for initiative and can see a creature

**Requirements** You're a master in Stealth.

This small, matte-black pin always seems to be on the periphery of your vision, even when you stare directly at it. When you Activate the talisman, choose one creature you can see. You become [[Invisible]] to that creature unless it succeeds at a DC 28 [[Will]] save. This effect lasts for 1 minute or until the target hits you with an attack, whichever comes first.

**Source:** `= this.source` (`= this.source-type`)
