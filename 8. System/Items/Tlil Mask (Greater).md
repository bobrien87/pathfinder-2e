---
type: item
source-type: "Remaster"
level: "9"
traits: ["[[Invested]]", "[[Magical]]"]
price: "{'gp': 600}"
usage: "wornmask"
bulk: "L"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Colorful, beaded *tlil masks* are commonly found on the distant continent of Arcadia, but trade between the two regions means that they can also be found in the Mwangi Expanse as curiosities. These masks usually bear floral patterns and attune your senses to plants of all varieties.

**Activate** `pf2:1` (concentrate)

**Frequency** once per day

**Effect** Your vision up to 60 feet sees through small amounts of living plant matter as though it were transparent. While this effect is active, creatures can't be [[Concealed]] from you due to living plants, such as small trees, vines, and grass. This also prevents them from Hiding or Sneaking past you using only living plants for concealment or cover. Other than the inability to use the cover to Hide or Sneak, this ability doesn't prevent plants from providing cover to creatures or blocking line of effect. It also doesn't allow you to see through dead plant matter, such as the wooden walls of a building, or thick plant matter, such as the walls of a dungeon built entirely inside an enormous living tree. The effect lasts for 10 minutes.

**Source:** `= this.source` (`= this.source-type`)
