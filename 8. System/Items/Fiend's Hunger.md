---
type: item
source-type: "Remaster"
level: "4"
traits: ["[[Agile]]", "[[Finesse]]", "[[Magical]]", "[[Thrown 10]]", "[[Versatile s]]"]
price: "{'gp': 100}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Season of Ghosts Hardcover Compilation"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

The blade of this *+1 low-grade silver dagger* has a sickly red tinge. Though once used to send souls to empower Kugaptee, the fury of those slain by the blade now allow its wielder to periodically strike back against fiends.

**Activate - Avenging Soul** `pf2:f` (concentrate, divine, mental)

**Frequency** once per day

**Trigger** You score a critical hit against a fiend

**Effect** Vengeful echoes of sacrificed souls lance out into the psyche of the fiend struck. After the normal effects of the critical hit, the target must roll a DC 18 [[Fortitude]] save.
- **Critical Success** The creature is unaffected.
- **Success** The creature becomes distracted by vengeful spirits and becomes [[Off Guard]] until the start of your next turn.
- **Failure** As success, but the creature is also [[Slowed]] 1 for 1 round.
- **Critical Failure** As failure, but the creature is slowed 1 for 1 minute.

**Source:** `= this.source` (`= this.source-type`)
