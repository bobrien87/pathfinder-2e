---
type: item
source-type: "Remaster"
level: "2"
traits: ["[[Alchemical]]", "[[Consumable]]", "[[Processed]]"]
price: "{'gp': 5}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** 10 minutes (manipulate)

This hot, broth-based soup typically contains tubers, leeks, zesty spices, reagents, and if desired, the meat of livestock. Civic authorities commission batches of mender's soup for workers if a tricky job is on the agenda. After you eat the soup, its effects last 24 hours or until you make your next daily preparations, whichever comes first. You gain a +1 item bonus to Crafting checks to Repair and restore an additional 5 Hit Points to items you successfully Repair during this time.

If you eat mender's soup over the entire period required to attempt a Crafting check to Craft (typically a minimum of eating the soup each day for 4 days), the +1 bonus from the soup can be applied to that check, too.

**Source:** `= this.source` (`= this.source-type`)
