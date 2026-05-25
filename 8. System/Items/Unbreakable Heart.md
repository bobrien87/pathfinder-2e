---
type: item
source-type: "Remaster"
level: "3"
traits: ["[[Invested]]", "[[Magical]]", "[[Tattoo]]"]
price: "{'gp': 60}"
usage: "tattooed-on-the-body"
bulk: "—"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

The name of your beloved adorns this stylized image of a heart. An unbreakable heart tattoo can be received only at the end of a successful [[Heartbond]] ritual, serving as your token. The other participant can have a token other than a tattoo if they wish. If you have more than one *heartbond*, each unbreakable heart you have serves as a token for only one of them. The love exuding from you grants you a +1 item bonus to Diplomacy checks. When you use *heartbond*'s activity to learn your beloved's present state, you can also grant them a small gift, choosing from the following options each time. Make your choice after learning their state.

- Your beloved gains 5 temporary Hit Points that last for 10 minutes.
- The tattoo casts [[Guidance]] on your beloved.
- The tattoo casts [[Stabilize]] on your beloved.
- The tattoo casts [[Light]] on your beloved's token from *heartbond*

**Source:** `= this.source` (`= this.source-type`)
