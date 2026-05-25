---
type: item
source-type: "Remaster"
level: "8"
traits: ["[[Divine]]", "[[Invested]]", "[[Tattoo]]"]
price: "{'gp': 425}"
usage: "tattooed-on-the-body"
bulk: "—"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Prerequisites** worshipper of a deity

You have marked your body to show your devotion to a deity. This tattoo could be the deity's religious symbol, another image that evokes that deity, or another mark you gained through your devotion. The tattoo serves as a silver religious symbol of the deity. Provided you keep the tattoo uncovered, you need not wield it to gain that benefit.

When you get the tattoo and aren't sanctified, you can choose to sanctify yourself to your deity.

If you cease meeting the prerequisites, the tattoo fades, and you lose its benefits until you perform an [[Atone]] ritual and meet the prerequisites thereafter.

**Activate** Cast a Spell

**Frequency** once per day

**Effect** The tattoo casts a 3rd-rank [[Harm]], [[Heal]], or the 3rd-rank spell from your deity's cleric spells. You can choose *harm* or *heal* only in accord with the deity's divine font. If the deity allows either spell, choose one the tattoo can cast when you receive the tattoo. The DC for any of these spells is 24.

**Source:** `= this.source` (`= this.source-type`)
