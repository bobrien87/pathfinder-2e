---
type: creature
group: ["Undead", "Unholy"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Wight"
level: "3"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Medium"
trait_01: "Undead"
trait_02: "Unholy"
trait_03: "Wight"
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+10; [[Darkvision]]"
languages: "Common, Necril"
skills:
  - name: Skills
    desc: "Athletics +10, Intimidation +9, Stealth +8"
abilityMods: ["+4", "+1", "+4", "+0", "+3", "+2"]
abilities_top:
  - name: "Grave Weapon"
    desc: "The wight is bound to a dagger it was buried with. Other wights can be bound to different weapons."
  - name: "Corrupting Spite"
    desc: "The wight's unarmed attacks and bound weapons inflict a curse that makes a creature grow weak and spiteful. If a wight inflicts corrupting spite on a creature already afflicted by it, the victim attempts a new save, ignoring the result if it's better than a failure. <br>  <br> A living humanoid that dies while under the curse rises as a wight after 1d4 rounds, controlled by the wight that killed it. The wight spawn can't inflict corrupting spite and is [[Clumsy]] 2. If its creator dies or after roughly a month of existence, the new wight becomes autonomous and turns into a normal wight <br>  <br> **Saving Throw** DC 17 [[Fortitude]] save; <br>  <br> **Stage 1** [[Drained]] 1 (1 round) <br>  <br> **Stage 2** [[Drained]] 2 and doesn't treat any creatures as allies (1 round) <br>  <br> **Stage 3** As stage 2, except [[Drained]] 3 (1 round) <br>  <br> **Stage 4** As stage 2, except [[Drained]] 4 (1 round)."
armorclass:
  - name: AC
    desc: "18; **Fort** +11, **Ref** +6, **Will** +10"
health:
  - name: HP
    desc: "40; fueled by spite, void healing; **Immunities** death effects, disease, paralyzed, poison, unconscious, bleed"
abilities_mid:
  - name: "Final Spite"
    desc: "`pf2:r` **Trigger** The wight is reduced to 0 Hit Points <br>  <br> **Effect** The wight makes a Strike before being destroyed. This Strike can inflict corrupting spite, but fueled by spite doesn't apply."
  - name: "Fueled by Spite"
    desc: "Each time a creature loses Hit Points due to a corrupting spite curse the wight inflicted, the wight gains 3 temporary Hit Points."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Claw +12 (`pf2:1`) (agile, unarmed), **Damage** 1d4+6 slashing plus [[Corrupting Spite]]"
  - name: "Melee strike"
    desc: "Dagger +12 (`pf2:1`) (agile, finesse, versatile s), **Damage** 1d4+6 piercing plus [[Corrupting Spite]]"
  - name: "Melee strike"
    desc: "Dagger +10 (`pf2:1`) (agile, thrown 10, versatile s), **Damage** 1d4+6 slashing plus [[Corrupting Spite]]"
spellcasting: []
abilities_bot: []
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

Wights are intelligent undead spawned through inescapable cycles of spite. This spite might come from their own malevolent will in life, or can be instilled by necromantic rituals, typically involving the desecration of burial sites. Wights usually haunt burial grounds, catacombs, or other places of the dead. Their hunger is targeted toward the living—those whose pumping hearts and ruddy warmth inspire visceral hatred.

As many types of wights exist as types of people from which they might be created. Hulking brutes, skittering sneaks, and cunning tinkers all make for different wights with different niches to fill. The environment, too, plays a part in determining a wight's special abilities and defenses. Frost wights, for instance, can be found in parts of the world where exposure is a common end and the resentment of being left alone in the wild is a common source of spite. Durable and sustained by void energy, wights can last in harsh environments without decaying the way some lesser undead do.

A single wight can wreak significant havoc if it is compelled to rise from its tomb. Because creatures slain under a wight's curse can become wights as well, all it takes is a single wight and a handful of unlucky graveyard visitors to create a veritable horde of these undead. Thus, canny priests and adventurers know that the best solution to a wight problem is swift and total eradication. Care must be taken, though, to destroy wight spawn before attempting to destroy the parent wight, for spawn without a master gain the ability to create spawn of their own.

```statblock
creature: "Wight"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
