---
type: item
source-type: "Remaster"
level: "6"
traits: ["[[Contract]]", "[[Invested]]", "[[Magical]]"]
price: "{'value': {}}"
usage: "other"
bulk: "—"
source: "Pathfinder Lost Omens Draconic Codex"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

You have exchanged your voice for the authority and breath of your bound dragon. Your voice echoes with the dragon's idiosyncrasies. You can cast fear as an innate spell once per day, with the spell's tradition matching that of your bound dragon.

Once per day, from any distance, your bound dragon can choose to take control of your voice. They dictate everything you say (or don't say) for up to 10 minutes. They can choose to speak in any language you or they know, though they can't use your voice to cast spells or activate items.

**Activate—Breath of the Dragon** `pf2:1` (concentrate)

**Frequency** once per day

**Effect** You exhale a torrent of energy in a @Template[type:cone|distance:30] or a @Template[type:line|distance:60], dealing @Damage[(@actor.level)d6|options:area-damage]{1d6 damage per level}. Each creature in the area must attempt a basic saving throw against the higher of your class DC or spell DC. You can't use this ability again for 1d4 rounds. The area, damage type, and type of saving throw match those of your Draconic Benefactor. This ability has the trait associated with the type of damage it deals.

[[Fortitude]] save [[Reflex]] save [[Will]] save

**Oathbreaker's Calamity** Should either party break the oath, your throat and mouth become swollen and elongated, preventing you from speaking any language but Draconic and causing any use of the Dragon Breath ability granted by this pact to also damage you. The dragon becomes [[Deafened]], but call still hear your voice.

**Source:** `= this.source` (`= this.source-type`)
