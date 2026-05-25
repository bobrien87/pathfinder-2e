---
type: creature
group: ["Monitor", "Psychopomp"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Nosoi"
level: "1"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Tiny"
trait_01: "Monitor"
trait_02: "Psychopomp"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+6; [[Darkvision]], [[Lifesense]] (precise) 60 feet"
languages: "Chthonian, Diabolic, Empyrean, Requian"
skills:
  - name: Skills
    desc: "Acrobatics +6, Performance +6, Religion +6, Society +2, Stealth +6, Boneyard Lore +8, Library Lore +8"
abilityMods: ["-1", "+3", "+1", "+1", "+1", "+3"]
abilities_top:
  - name: "Shepherd's Touch"
    desc: "A nosoi's Strikes have the benefit of a *[[Ghost Touch]]* property rune and deal an additional 1d6 void damage to living creatures or 1d6 vitality damage to undead."
armorclass:
  - name: AC
    desc: "16; **Fort** +4, **Ref** +8, **Will** +6"
health:
  - name: HP
    desc: "18; **Immunities** death effects, disease; **Resistances** void 3, poison 3"
abilities_mid: []
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Beak +6 (`pf2:1`) (finesse, magical, reach 0 ft., unarmed), **Damage** 1d4-1 piercing plus [[Spirit Touch]]"
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 16, attack +8<br>**4th** [[Read Omens]], [[Talking Corpse]]<br>**2nd** [[Invisibility (At Will, Self Only)]], [[Noise Blast]]"
abilities_bot:
  - name: "Change Shape"
    desc: "`pf2:1` The nosoi takes the appearance of a raven or songbird. This doesn't change its Speed or its attack and damage modifiers with its Strikes. <br>  <br> The monster changes its shape indefinitely. It can use this action again to return to its natural shape or adopt a new shape. Unless otherwise noted, a monster cannot use Change Shape to appear as a specific individual. Using Change Shape counts as creating a disguise for the [[Impersonate]] use of Deception. The monster's transformation automatically defeats Perception DCs to determine whether the creature is a member of the ancestry or creature type into which it transformed, and it gains a +4 status bonus to its Deception DC to prevent others from seeing through its disguise. Change Shape abilities specify what shapes the monster can adopt. The monster doesn't gain any special abilities of the new shape, only its physical form. For example, in each shape, it replaces its normal Speeds and Strikes, and might potentially change its senses or size. Any changes are listed in its stat block."
  - name: "Haunting Melody"
    desc: "`pf2:1` The nosoi croons an entrancing song. Each living or undead creature within a @Template[emanation|distance:60] must attempt a DC 18 [[Will]] save. The effect lasts until the end of the nosoi's next turn, but the nosoi can Sustain it. A creature that succeeds at its save is temporarily immune for 24 hours. Despite being a mental effect, this ability affects mindless undead. <br>  <br> Psychopomps are immune to this ability. <br> - **Failure** The creature is [[Fascinated]] with the nosoi. <br> - **Critical Failure** The creature is fascinated with the nosoi and must spend each of its actions on its turn to move closer to the nosoi as expediently as possible while avoiding obvious dangers. If a fascinated creature is adjacent to the nosoi, it stays still and doesn't act. If the creature is attacked, the fascination ends."
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

A nosoi resembles a whippoorwill, sparrow, or other small bird wearing a heavy leather plague doctor's mask. They are the clerks, messengers, and scribes of the Boneyard, witnessing judgments, directing souls, and generally performing the administrative grunt work that keeps the Boneyard functioning. Most nosois are particularly chatty and eager to discuss how important they consider their individual assignments to be.

Psychopomps are guardians and shepherds of the dead in the Boneyard, the vast plane of graves where mortal souls are judged and sent on to their eternal rewards or damnations. Psychopomps ensure that the dead come to terms with their transition from mortality and are properly sorted into the appropriate afterlife. They also protect souls from being preyed upon by supernatural predators. Nearly all psychopomps wear masks, especially when they're likely to be interacting with mortals, although the types of masks they wear are as varied as the psychopomps themselves. The courts of the Boneyard preside in Requian, a somber yet melodic language spoken slowly with various tonal shifts.

Many psychopomps are intimately involved with the Boneyard's massive bureaucracy. Few pursue mercy, justice, or personal gain; their duties to Pharasma and her Boneyard are supreme. Nevertheless, individual psychopomps interpret their duties in different ways, which might put them in conflict with mortals or even with each other.

```statblock
creature: "Nosoi"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
