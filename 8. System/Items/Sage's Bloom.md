---
type: item
source-type: "Remaster"
level: "5"
traits: ["[[Consumable]]", "[[Magical]]", "[[Talisman]]"]
price: "{'gp': 50}"
usage: "affixed-to-headgear"
bulk: "L"
source: "Pathfinder #202: Severed at the Root"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** `pf2:f` (concentrate)

**Trigger** You attempt a Nature check to [[Recall Knowledge]] but haven't rolled

**Requirements** You're trained in Nature.

This simple white flower is placed into a hat or worn braided into your hair. When activated, it releases a soothing scent, which helps you focus your mind. When you activate the talisman, you Recall Knowledge three times, rather than once. If you use Nature for any of these checks and get a critical failure, that check is instead a failure.

**Source:** `= this.source` (`= this.source-type`)
