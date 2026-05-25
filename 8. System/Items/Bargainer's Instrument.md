---
type: item
source-type: "Remaster"
level: "15"
traits: ["[[Consumable]]", "[[Magical]]"]
price: "{'gp': 1000}"
usage: "held-in-two-hands"
bulk: "L"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** 1 hour (concentrate, manipulate)

A bargainer's instrument is a musical implement. The most typical version is a violin made from maple and spruce, its body stained so deep a purple it appears almost black. When activated, the instrument casts a [[Binding Circle]] ritual to conjure a willing extraplanar talent to compete with you in performance.

The contest could be a musical battle, a dance-off, an oratorical debate—the two of you could even use entirely different types of performance. The loser of the bout is magically bound to perform a task of the winner's choice within 1 week. The contest consists of taking turns to [[Perform]], starting with your opponent. The Performance check's DC is the higher of the opponent's Perception DC or Will DC, though the two parties can mutually agree to use an impartial judge instead. The first to reach four successes wins, with each critical successes counting as two successes. If you play the bargainer's instrument as part of your performance, it grants you a +2 item bonus to the Performance checks.

After the contest, the conjured creature can choose to return to where it came from or remain where you conjured it. The loser must endeavor to complete the task by all reasonable means within 1 week. Failing to complete it is shameful but has no further consequences. The instrument loses its magic and remains a non-magical virtuoso instrument.

**Source:** `= this.source` (`= this.source-type`)
