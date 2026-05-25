---
type: creature
group: ["Monitor", "Psychopomp"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Shoki"
level: "9"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Medium"
trait_01: "Monitor"
trait_02: "Psychopomp"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+21; [[Darkvision]], [[Lifesense]] (precise) 60 feet"
languages: "Chthonian, Diabolic, Empyrean, Requian (Truespeech)"
skills:
  - name: Skills
    desc: "Deception +20, Diplomacy +20, Intimidation +20, Occultism +16, Religion +19, Society +16, Stealth +14, Boneyard Lore +19"
abilityMods: ["+4", "+1", "+4", "+3", "+6", "+5"]
abilities_top:
  - name: "Constant Spells"
    desc: "A constant spell affects the monster without the monster needing to cast it, and its duration is unlimited. If a constant spell gets counteracted, the monster can reactivate it by spending the normal spellcasting actions the spell requires."
  - name: "Infuse Staff"
    desc: "A shoki's staff becomes a +1 striking staff and is treated as if it were adamantine while the shoki wields it. A shoki's staff has Hardness 14 and HP 56 (BT 28) while possessed by the shoki and Hardness 5 and HP 20 (BT 10) while out of the shoki's possession. A shoki whose staff is taken or destroyed can infuse a new one with an hour of work."
  - name: "Shepherd's Touch"
    desc: "A shoki's Strikes affect incorporeal creatures with the effects of a *[[Ghost Touch]]* property rune and deal 2d6 void damage to living creatures and 2d6 vitality damage to undead."
armorclass:
  - name: AC
    desc: "27; **Fort** +19, **Ref** +14, **Will** +21"
health:
  - name: HP
    desc: "150; **Immunities** death effects, disease; **Resistances** poison 10, void 10"
abilities_mid:
  - name: "+1 Status to All Saves vs. Magic"
    desc: ""
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Staff +19 (`pf2:1`) (monk, two hand d8), **Damage** 2d4+6 bludgeoning plus [[Shepherds Touch]]"
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 28, attack +20<br>**7th** [[Interplanar Teleport (Self and locked soul only; to the Boneyard only)]]<br>**6th** [[Spirit Blast]]<br>**5th** [[Mind Probe]], [[Truespeech]] (Constant)<br>**4th** [[Read Omens]]<br>**3rd** [[Holy Light]]<br>**2nd** [[Calm]], [[Invisibility (At Will; Self Only)]]<br>**1st** [[Detect Magic]], [[Frostbite]], [[Heal]], [[Read Aura]], [[Stabilize]], [[Vitality Lash]]"
abilities_bot:
  - name: "Soul Lock"
    desc: "`pf2:2` **Requirements** The shoki doesn't have a soul locked within their staff <br>  <br> **Effect** The shoki attempts to capture the soul of a creature on the brink of death: an undead creature, a creature with the dying condition, or a creature that died within the last minute. The target must attempt a DC 32 [[Will]] save with the following results. <br> - **Critical Success** The creature is unaffected and becomes temporarily immune to Soul Lock. <br> - **Success** The shoki's staff tugs at the creature's soul but doesn't trap it. If the creature is living, it becomes [[Doomed]] 1 (or increases its doomed condition by 1). If the creature is a corporeal undead, it becomes [[Enfeebled]] 2. If the creature is an incorporeal undead, it becomes [[Stupefied 2]]. The creature then becomes temporarily immune to Soul Lock for 24 hours. <br> - **Failure** The shoki captures the creature's soul in its staff. If the creature is living, it dies. If the creature is a corporeal undead, its body becomes an inanimate corpse. While the soul is locked in the staff, the target can't be returned to life or undeath or rejuvenate through any means, save for powerful magic, such a wish ritual. If the shoki's staff is destroyed or the shoki wills it, the soul is released. A shoki's staff can only hold one soul at a time."
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

Shokis shepherd wayward souls to the Boneyard. They take great pride in traveling to the Universe (and sometimes beyond) to hunt down those who have evaded Pharasma's judgment, whether they be malicious foes or unfortunate undead. A shoki is often transported closer to their quarry by a more powerful psychopomp, but they have the ability to return once they've completed their mission.

A shoki resembles an aged humanoid with jet-black skin, curling ram's horns, and a large snail's shell on their back. Some believe that a shoki keeps souls within that shell for transport back to the Boneyard, while in reality, that power resides in their infused staff.

Many psychopomps are intimately involved with the Boneyard's massive bureaucracy. Few pursue mercy, justice, or personal gain; their duties to Pharasma and her Boneyard are supreme. Nevertheless, individual psychopomps interpret their duties in different ways, which might put them in conflict with mortals or even with each other.

```statblock
creature: "Shoki"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
