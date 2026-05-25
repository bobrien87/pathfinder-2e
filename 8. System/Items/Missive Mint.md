---
type: item
source-type: "Remaster"
level: "1"
traits: ["[[Alchemical]]", "[[Auditory]]", "[[Consumable]]", "[[Linguistic]]"]
price: "{'gp': 3}"
usage: "held-in-one-hand"
bulk: "—"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** `pf2:1` Interact

This white mint with a chalky coating appears to be a normal candy unless someone examining it succeeds at a DC 15 [[Crafting]] check to Identify Alchemy. If the crafter has the powerful alchemy class feature, this DC is their class DC instead, if it's higher. The mint's crafter can imbue a missive mint with a message containing up to 25 words while creating it. Someone who consumes the missive mint hears the message in a fizzing voice as the mint's coating bubbles away, which takes the same amount of time as it would to speak the message. The mint's eater has no way of knowing who the original sender was, what they sound like, or who the message was intended for.

**Source:** `= this.source` (`= this.source-type`)
