---
type: creature
group: ["Human", "Humanoid"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Cultist"
level: "1"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Medium"
trait_01: "Human"
trait_02: "Humanoid"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+4"
languages: "Common"
skills:
  - name: Skills
    desc: "Deception +3, Intimidation +3, Occultism +4, Society +4, Stealth +6, Cult Lore (for the cultist's own cult) +8"
abilityMods: ["+4", "+3", "+2", "+1", "-1", "+0"]
abilities_top: []
armorclass:
  - name: AC
    desc: "17; **Fort** +7, **Ref** +8, **Will** +4 (or +2 vs. higher-ranking members of the cult)"
health:
  - name: HP
    desc: "20"
abilities_mid:
  - name: "Will +2 vs. Higher Ranking Members of the Cult"
    desc: ""
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Dagger +7 (`pf2:1`) (agile, versatile s), **Damage** 1d4+4 piercing"
  - name: "Melee strike"
    desc: "Dagger +6 (`pf2:1`) (agile, thrown 10, versatile s), **Damage** 1d4+4 piercing"
  - name: "Melee strike"
    desc: "Fist +7 (`pf2:1`) (agile, nonlethal, unarmed), **Damage** 1d4+4 bludgeoning"
spellcasting: []
abilities_bot:
  - name: "Fanatical Frenzy"
    desc: "`pf2:1` **Requirements** The cultist has taken damage and is neither [[Fatigued]] nor already in a frenzy <br>  <br> **Effect** The cultist flies into a frenzy that lasts 1 minute. While frenzied, the cultist gains a +1 status bonus to attack rolls and a +2 status bonus to damage rolls, and they take a –2 penalty to AC. The cultist can't voluntarily stop their frenzy. After their frenzy, the cultist is fatigued."
sourcebook: "NPC Core"
source-type: "Remaster"
---
### `= this.file.name`

Cultists have passed an initiation ritual to a secret sect or organization; now, they devote themselves to achieving their most perfect spiritual form.

Hidden secrets and occult powers have an irresistible lure for many. Since the majority of these NPCs are spellcasters, consider using alternative spell lists to adjust their themes.

```statblock
creature: "Cultist"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
