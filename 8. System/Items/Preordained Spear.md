---
type: item
source-type: "Remaster"
level: "9"
traits: ["[[Magical]]", "[[Monk]]", "[[Mythic]]", "[[Thrown 20]]"]
price: "{'gp': 700}"
usage: "held-in-one-hand"
bulk: "1"
source: "Pathfinder #218: Titanbane"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This *+1 striking spear* seems to know when its wielder is about to die. Its wooden body bears countless carvings, leaving it thinner than most spears. While you are [[Doomed]], a *preordained spear* glows with a faint red light that gives you a haunted look and sheds dim light within 5 feet.

**Activate—Delay Doom** `pf2:1` (manipulate)

**Requirements** Your name is not on the spear, and you have the doomed condition

**Effect** Your name appears on the shaft of the *preordained spear*. Your doomed value decreases by 1, and you regain 1 Mythic Point. Your name fades from the spear the next time you make your daily preparations.

**Source:** `= this.source` (`= this.source-type`)
