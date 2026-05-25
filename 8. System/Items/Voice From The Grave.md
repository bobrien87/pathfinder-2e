---
type: item
source-type: "Remaster"
level: "10"
traits: ["[[Magical]]", "[[Mental]]"]
price: "{'gp': 1700}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This onyx skull emits eerie whispers when on its own, but when held the skull enables you to speak with spirits and haunts you can see, even if you don't share a language. The voice from the grave translates anything the spirit or haunt says, using a language you understand, and translates your words for the spirit or haunt in kind. This doesn't make the target friendly or even cooperative, but it does enable communication. The GM determines the language in the case of a haunt. You can't communicate with mindless spirits using the skull.

**Activate** `pf2:2` (concentrate)

**Frequency** once per hour

**Effect** The onyx skull casts a DC 27 [[Charm]] spell on one spirit or haunt you can communicate with using the skull. If you target a haunt that doesn't have a Will modifier, it automatically gets a failure on its save.

**Source:** `= this.source` (`= this.source-type`)
