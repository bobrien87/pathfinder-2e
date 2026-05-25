---
type: item
source-type: "Remaster"
level: "5"
traits: ["[[Magical]]"]
price: "{'gp': 125}"
usage: "etched-onto-armor"
bulk: "—"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Your armor provides support for your joints or advanced prostheses for missing limbs, holding your body in place and easing physical symptoms. This replicates the benefits of any number of splints, supports, and prostheses. When you invest the armor, you determine how many such supports you want, and where on your body they assist you.

In addition, the extra support and structure provided by the armor allows you to transport more than you would otherwise normally be able to. You can carry Bulk equal to 6 + your Strength modifier before becoming encumbered, and you can hold and carry a total Bulk of up to 11 + your Strength modifier.

**Source:** `= this.source` (`= this.source-type`)
