---
type: item
source-type: "Remaster"
level: "20"
traits: ["[[Cursed]]", "[[Grimoire]]", "[[Magical]]"]
price: "{'value': {}}"
usage: "other"
bulk: "L"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

The origins of the notorious *Dullahan Codex* are shrouded in mystery. Some legends claim it belongs to a dullahan whose head was taken by the Grim Reaper. Others attribute its creation to a powerful necromancer whose name has been lost to time. Whatever the truth, the grimoire has passed down through the ages, sometimes via mortal hands and other times mysteriously appearing among the possessions of its next target. It deserves its reputation for dooming those who possess it to die, but scholars debate whether the codex causes this fate or merely acts as its harbinger.

The *Dullahan Codex* is a jet-black tome bearing a single rune embossed on its cover, and it functions as a true endless grimoire. Inside, scrawled across its parchment pages in a delicate, spidery script, is a lengthy list of names that always appears in a reader's native alphabet. The grimoire isn't sentient, but it selects its owners, quickly passing out of the hands of those it doesn't choose. An intended victim's name appears on the list of names.

If your name is on the list and you touch the volume or read from its pages, you must attempt a DC 45 [[Will]] save.
- **Critical Success** The codex disappears, moving on to a new victim.
- **Success** The codex fuses to you.
- **Failure** The codex fuses to you, and you become [[Doomed]] 1.
- **Critical Failure** As failure, but you're [[Doomed]] 2.

If you attempt to get rid of the codex while it's fused to you, it returns to your possession within an hour. Each day the codex is fused to you, you must attempt another Will saving throw, but a critical success does nothing. The doomed value from the codex can decrease only after it's no longer fused to you; once it's fused to you, you remain its intended victim unless you complete a [[Freedom]] ritual aimed at ending this 10th-rank effect. (On a critical failure with this ritual, the codex adds all casters to its list.) You can redirect the curse by inscribing another person's name in the grimoire and succeeding at a DC 40 [[Arcana]] check or DC 40 [[Occultism]] check. Doing so is an unholy act, anathema to many deities. If the curse is ritually ended or redirected, or the chosen victim dies, the codex moves on to a new victim.

**Source:** `= this.source` (`= this.source-type`)
