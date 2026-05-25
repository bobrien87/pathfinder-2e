---
type: item
source-type: "Remaster"
level: "15"
traits: ["[[Cursed]]", "[[Magical]]"]
price: "{'value': {}}"
usage: "held-in-two-hands"
bulk: "1"
source: "Pathfinder Dark Archive (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This massive tome's yellowed pages curl at the edges, and the letters on its face and spine are too worn to be read. When you open the book, it always opens to a page that seems to perfectly answer the question you had in mind, but reading more than a few lines causes your head to swim alarmingly.

**Activate—Study Memory** 1 hour (concentrate, manipulate)

**Requirements** You aren't drained

**Effect** You open the book while trying to learn information about any topic. *The Book of Lost Days* permits you to view another's memory, which contains information about that subject commensurate to rolling a total of 40 to [[Recall Knowledge]] about the topic, with additional context provided on a success or critical success.

The price for this knowledge is the memory of a day in your past, and the vitality of a day in your future. You lose the memory of that day completely, and the total of all the knowledge you learned on that date is added to the book's repository of information. The book, not you, chooses which memories are taken, preferring days with concentrated emotional resonance, and thus tends to steal significant life moments. This loss affects only your memories; it has no effect on your level, class, feats, or other character choices.

Your natural lifespan is also shortened by 1 day. The loss of this life energy causes you to be [[Drained]] 2. You can't reduce the drained condition for 2 days, after which you can recover normally from the condition.

Creatures have occasionally managed to use the *Book of Lost Days* not to gain others' knowledge but to wipe their minds clean of painful memories or deadly secrets. Their memories aren't destroyed but merely stored in the book, where someone else might later retrieve them.

**Source:** `= this.source` (`= this.source-type`)
