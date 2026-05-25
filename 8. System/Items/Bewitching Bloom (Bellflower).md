---
type: item
source-type: "Remaster"
level: "7"
traits: ["[[Invested]]", "[[Magical]]", "[[Tattoo]]"]
price: "{'gp': 350}"
usage: "tattooed-on-the-body"
bulk: "—"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

While dormant, this tattoo appears to be a simple flower bud, but when activated the flower swiftly blossoms, remaining that way until the next time you make your daily preparations. These blooms are colorful, elegant representations of bellflowers.

**Activate** `pf2:2` envision

**Frequency** once per day

**Effect** Choose a willing ally you can see within 30 feet. A need for freedom trills through your ally's blood. Until the end of that ally's next turn, they gain a +2 status bonus to rolls to recover from the [[Confused]], frightened, [[Grabbed]], [[Paralyzed]], and [[Restrained]] conditions. When you Activate the bloom, the target can attempt a new save against a condition the bonus applies to, or they can use a reaction to attempt to [[Escape]] being grabbed, [[Immobilized]], or restrained, provided such an attempt is allowed.

**Source:** `= this.source` (`= this.source-type`)
