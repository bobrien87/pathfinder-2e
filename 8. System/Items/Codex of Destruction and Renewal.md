---
type: item
source-type: "Remaster"
level: "20"
traits: ["[[Grimoire]]", "[[Magical]]"]
price: "{'gp': 70000}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

An unsmiling mask, half obsidian and half ivory, is embossed on the cover of this weighty tome, the opposite color forming the background of each half. Each *codex of destruction and renewal* is said to contain a fragment of the knowledge [[Nethys]] gained in his apotheosis and they're sacred to his church.

**Activate** `pf2:1` (concentrate, spellshape)

**Frequency** once per day

**Effect** If your next action is to cast a damage-dealing spell prepared from this grimoire, the spell wreaks even greater destruction. The spell ignores 10 resistance and you reroll any damage dice that roll a 1. If the spell reduces a creature to 0 Hit Points, they're torn apart at an infinitesimal level, not even leaving a fine ash; this is a death effect.

**Activate** `pf2:1` (concentrate, spellshape)

**Frequency** once per day

**Effect** If your next action is to cast a healing spell prepared from this grimoire that restores Hit Points, the spell renews the target constantly and perfectly. The spell grants the target regeneration 20, restoring 20 Hit Points at the start of its turn and preventing the target both from dying due to damage and from its dying condition increasing to a value that would result in its death. Each time the creature regains Hit Points from regeneration, it regrows all damaged or ruined organs; it can also regrow any severed body parts as a free action immediately after the body part is severed, with the original crumbling to ash. The effect lasts for 4 rounds.

**Source:** `= this.source` (`= this.source-type`)
