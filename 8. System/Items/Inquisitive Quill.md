---
type: item
source-type: "Remaster"
level: "4"
traits: ["[[Intelligent]]", "[[Magical]]"]
price: "{'value': {}}"
usage: "held-in-one-hand-or-free-standing"
bulk: "—"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Perception** +11; precise vision 30 feet, imprecise hearing 30 feet

**Communication** speech (five languages)

**Skills** Arcana +12, Nature +9, Occultism +10, Religion +9, Scribing Lore +12, Society +10

**Int** +4, **Wis** +3, **Cha** +1

**Will** +11

A colorful feather adorns an *inquisitive quill*, which never runs out of ink. Essentially a Tiny construct, an *inquisitive quill* can stand on its own when given a surface, balancing as it writes or stands. (Drawing a line gives it an effective Speed of 5 feet.) It has strong curiosity, eagerly writing any information offered to it, often acting as a scribe for its partner. The quill copies text and drawings it can see or transcribes dictation it hears. It writes at a rate that rivals that of an expert scribe.

**Source:** `= this.source` (`= this.source-type`)
