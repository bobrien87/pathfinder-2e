---
type: creature
group: ["Human", "Humanoid"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "World Ender"
level: "16"
rare_01: "Rare"
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
    desc: "+25"
languages: "Common"
skills:
  - name: Skills
    desc: "Intimidation +28, Nature +27, Religion +25, Society +27"
abilityMods: ["+4", "+3", "+7", "+7", "+3", "+2"]
abilities_top: []
armorclass:
  - name: AC
    desc: "36; **Fort** +30, **Ref** +26, **Will** +28"
health:
  - name: HP
    desc: "275; **Resistances** fire 15"
abilities_mid:
  - name: "Unyielding Purpose"
    desc: "`pf2:r` **Trigger** The world ender would be reduced to 0 HP <br>  <br> **Requirements** The world ender has a [[Volcanic Eruption]] spell remaining <br>  <br> **Effect** The world ender refuses to let their destructive dream go unrealized, stabilizing at 1 HP just long enough to cast *volcanic eruption*, centered on themself. They die, immolated in the eruption."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Fist +27 (`pf2:1`) (agile, nonlethal, unarmed), **Damage** 1d4+10 bludgeoning plus 3d6 fire"
  - name: "Melee strike"
    desc: "Staff of Fire +28 (`pf2:1`) (magical, two hand d8), **Damage** 2d4+10 bludgeoning plus 3d6 fire"
spellcasting:
  - name: "Primal Prepared Spells"
    desc: "DC 41, attack +33<br>**8th** (4 slots) [[Desiccate]], [[Punishing Winds]], [[Sunburst]], [[Sunburst]]<br>**7th** (4 slots) [[Blazing Bolt]], [[Fiery Body]], [[Volcanic Eruption]], [[Volcanic Eruption]]<br>**6th** (4 slots) [[Chain Lightning]], [[Chain Lightning]], [[Floating Flame]], [[Wall of Fire]]<br>**5th** (4 slots) [[Fireball]], [[Fireball]], [[Magic Passage]], [[Wall of Stone]]<br>**4th** (4 slots) [[Fly]], [[Fly]], [[Unfettered Movement]], [[Unfettered Movement]]<br>**3rd** (4 slots) [[Earthbind]], [[Earthbind]], [[Haste]], [[Slow]]<br>**2nd** (4 slots) [[Darkvision]], [[Enlarge]], [[Revealing Light]], [[Water Walk]]<br>**1st** (4 slots) [[Air Bubble]], [[Fleet Step]], [[Gentle Landing]], [[Gust of Wind]]<br>**Cantrips** [[Caustic Blast]], [[Electric Arc]], [[Gouging Claw]], [[Ignition]], [[Light]]"
abilities_bot:
  - name: "Monologue"
    desc: "`pf2:0` **Frequency** once per round <br>  <br> **Effect** Throughout combat, the world ender ceaselessly expounds upon the righteous reasons for their destructive aims and the futility of their enemies' efforts to stop them. They gain a +1 status bonus to Will saves and a +2 status bonus to damage rolls with their spells. Each time they take this action again, the bonuses increase by 1 and 2, respectively. The monologue ends (and the bonuses are lost) if the world ender becomes unable to act or speak, or if they end their turn without having taken this action."
  - name: "Overwhelming Energy"
    desc: "`pf2:1` If the next action the world ender uses is to Cast a Spell, the spell ignores 20 resistance to energy damage. This applies to all damage the spell deals, including persistent damage and damage caused by an ongoing effect of the spell. A creature's immunities are unaffected."
sourcebook: "NPC Core"
source-type: "Remaster"
---
### `= this.file.name`

Unlike most villains, world enders are unburdened by nuance. Their ultimate goal is simple, if lofty: destroy the world and everyone in it.

Villains pursue selfish and cruel goals, trampling over anyone in their way.

```statblock
creature: "World Ender"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
