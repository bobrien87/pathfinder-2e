---
type: item
source-type: "Remaster"
level: "9"
traits: ["[[Contract]]", "[[Invested]]", "[[Magical]]"]
price: "{'value': {}}"
usage: "held-in-one-hand"
bulk: "—"
source: "Pathfinder Lost Omens Draconic Codex"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

The oath that ties you to your bound dragon transcends the boundaries of life and death. When the pact is made, the dragon chooses one type of creature other than humanoid. (The GM selects the appropriate trait.) You gain resistance equal to half your level to physical and mental damage from these creatures. You also gain the Draconic Precision action. If you die from damage delivered by a creature of this type, you rise as an undead creature of the dragon's choice. This undead's level can be no higher than your level or your bound dragon's, whichever is lower. This undead creature has your mind; if it's normally mindless, it loses that trait and any immunity to mental.

**Draconic Precision** `pf2:1` (concentrate)

**Frequency** once per day

**Effect** Your Strikes against the chosen type of enemy deal an additional 1d6 precision damage for 1 minute. This damage increases to 2d6 if you're 17th level or higher.

**Oathbreaker's Calamity** Should either party break the oath, both you and the dragon are forever forsworn from comradery. Creatures can't treat either of you as an ally while in combat.

**Source:** `= this.source` (`= this.source-type`)
