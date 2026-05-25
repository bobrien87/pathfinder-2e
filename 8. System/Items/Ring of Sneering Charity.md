---
type: item
source-type: "Remaster"
level: "7"
traits: ["[[Cursed]]", "[[Invested]]", "[[Magical]]"]
price: "{'value': {}}"
usage: "wornring"
bulk: "—"
source: "Pathfinder Dark Archive (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This gold ring seems to offer good fortune to the wearer when they're charitable to those in need, but its curse was created to tear societies apart by inflaming class resentments and discrediting good works of true charity.

Upon donning the ring, you must attempt a secret DC 25 [[Will]] save to avoid activating its magic. If you succeed, the ring's curse remains dormant, and it appears to be an exhausted item with no magic left. If you fail, the curse awakens, and the ring fuses to you.

You're compelled to spend 10% of your wealth—and 10% of any future wealth you obtain—on charity. However, your acts of charity are insensitive and so insulting that they earn the recipients' enmity. For example, upon learning someone lost a child, you might toss money at them "to buy a new one." You can't understand why your gifts aren't met with gratitude and resent the unappreciative recipients, and you firmly believe you should be able to call upon them for favors. You consider yourself an ideal philanthropist, and you constantly try to ingratiate yourself with other charitable organizations and individuals by offering to guide their donations to be more like your own.

**Source:** `= this.source` (`= this.source-type`)
