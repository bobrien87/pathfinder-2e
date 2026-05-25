---
type: item
source-type: "Remaster"
level: "5"
traits: ["[[Divine]]", "[[Invested]]", "[[Magical]]"]
price: "{'gp': 150}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder #218: Titanbane"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This reversible doll shows Iapholi on one side and the harpy Ekriathe who preceded her in her line of reincarnation on the other. Non-magical successor dolls are popular gifts for children, and Iapholi often distributes them (including a handful of magical versions) on her birthday. Magical successor dolls sometimes frown, smile, or wink as if aware of their surroundings and nearby conversations.

**Activate—Big Eyes, Pleading Face** `pf2:r` (concentrate, emotion, mental, visual)

**Frequency** once per day

**Trigger** You fail or critically fail to [[Request]] a favor

**Effect** The doll's eyes grow large as its lips quiver, expressing adorable disappointment. Roll `gmr 1d4` and add the result to your Diplomacy check as a circumstance bonus, which might improve the degree of success.

**Activate—Fierce Gaze, Approving Smile** `pf2:r` (concentrate, emotion, mental, visual)

**Frequency** once per day

**Trigger** You succeed or critically succeed when [[Coercing]] a creature

**Effect** The doll smugly smirks at the creature, either reinforcing how wise it is to heed your demands or innocently reminding it how much happier it is for complying. After the creature finishes following your directives, it must attempt a DC 21 [[Will]] save.
- **Success** The creature is unaffected.
- **Failure** The creature's fond memory of the doll's approval overwhelms any hard feelings the creature has toward you; it doesn't act against you as a result of your coercion unless your demands were truly shocking (such as forcing them to violate any anathema they have or betray a close ally).

**Source:** `= this.source` (`= this.source-type`)
