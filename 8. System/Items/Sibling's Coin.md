---
type: item
source-type: "Remaster"
level: "1"
price: "{'gp': 10}"
usage: "held-in-one-hand"
bulk: "—"
source: "Pathfinder Dark Archive (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Access** Member of a secret society

Contrary to widespread belief, secret handshakes are not the preferred method of confirmation between secret society members, mostly because this would be obvious in the middle of a crowded street or busy tavern. Instead, societies tend to mark each other by carrying sibling's coins. The name was originally coined by a past secret society that has since fallen into obscurity, but its ingenious coins remain. The coins are innocuous, resembling common silver coins until the owner twists the outer edge clockwise. At this point, the face of the coin rotates to reveal the symbol of the secret society of the owner. Suspected compatriots often toy with their coins as a half-recognized fidget, before trying to subtly flash the inscription to their fellow conversationalist.

While it's possible to notice the coin's mechanism if you specifically check the coin (DC 20 [[Perception]] check), few people individually inspect coins unless they have a reason to be suspicious of them.

**Source:** `= this.source` (`= this.source-type`)
