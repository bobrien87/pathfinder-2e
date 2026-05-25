---
type: creature
group: ["Monitor", "Psychopomp"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Catrina"
level: "5"
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
    desc: "+13; [[Darkvision]], [[Lifesense]] (precise) 60 feet"
languages: "Chthonian, Diabolic, Empyrean, Requian (Telepathy 120 feet, Truespeech)"
skills:
  - name: Skills
    desc: "Acrobatics +14, Diplomacy +14, Intimidation +14, Medicine +12, Occultism +11, Religion +12, Boneyard Lore +11"
abilityMods: ["+0", "+5", "+4", "+2", "+4", "+5"]
abilities_top:
  - name: "Telepathy 120 feet"
    desc: "A monster with telepathy can communicate mentally with any creatures within the listed radius, as long as they share a language. This doesn't give any special access to their thoughts, and communicates no more information than normal speech would."
  - name: "Constant Spells"
    desc: "A constant spell affects the monster without the monster needing to cast it, and its duration is unlimited. If a constant spell gets counteracted, the monster can reactivate it by spending the normal spellcasting actions the spell requires."
  - name: "Shepherd's Touch"
    desc: "A catrina's Strikes affect incorporeal creatures with the effects of a *[[Ghost Touch]]* property rune and deal 1d6 void damage to living creatures and 1d6 vitality damage to undead."
armorclass:
  - name: AC
    desc: "22; **Fort** +11, **Ref** +12, **Will** +13"
health:
  - name: HP
    desc: "75; **Immunities** death effects, disease; **Resistances** poison 5, void 5"
abilities_mid:
  - name: "+1 Status to All Saves vs. Magic"
    desc: ""
  - name: "Calming Presence"
    desc: "30 feet. A creature that begins its turn within the area must attempt a DC 18 [[Will]] save. <br> - **Critical Success** The creature is unaffected and is temporarily immune to calming presence for 24 hours. <br> - **Success** The creature's attack rolls take a –1 status penalty for 1 round. <br> - **Failure** Any emotion effects that would affect the creature are suppressed, and the creature can't use hostile actions. If the creature is subjected to hostility from any other creature, it ceases to be affected by calming presence and is temporarily immune to calming presence for 24 hours. <br> - **Critical Failure** As failure, but hostility doesn't end the effect."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Fist +14 (`pf2:1`) (agile, finesse), **Damage** 2d8+2 bludgeoning plus [[Spirit Touch]]"
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 22, attack +14<br>**5th** [[Truespeech]] (Constant)<br>**4th** [[Talking Corpse]] (At Will), [[Translocate]]<br>**2nd** [[Invisibility (At Will, Self Only)]]<br>**1st** [[Illusory Disguise]], [[Light]]"
abilities_bot:
  - name: "Compel Condemned"
    desc: "`pf2:1` The catrina telepathically compels a creature within 30 feet to approach and allow the catrina to kiss them, in preparation for using Kiss of Death. The target must attempt a DC 22 [[Will]] save. <br> - **Success** The creature is unaffected and is temporarily immune to Compel Condemned for 24 hours. <br> - **Failure** The creature must spend each of its actions to move closer to the catrina as quickly as possible while avoiding obvious dangers. If the compelled creature is adjacent to the catrina, it stays still and doesn't act. If the creature takes any damage, the effect ends and the creature is temporarily immune to Compel Condemned for 24 hours. This effect lasts for 1 round, but if the catrina uses this ability again on subsequent rounds, it extend the duration by 1 round for all affected creatures. <br> - **Critical Failure** As failure, but damage does not end the effect."
  - name: "Kiss of Death"
    desc: "`pf2:2` The catrina gives a long, passionate kiss to an [[Unconscious]] or willing creature, dealing 3d6 void damage. Any creature damaged by the same catrina's Kiss of Death for 3 consecutive rounds becomes unconscious and is dying 1."
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

Not all spirits who enter the Boneyard realize they have died. Catrinas meet these souls, helping to convince them of the finality of their fate to ease a spirit's passing. Catrinas are more likely to intervene when a mortal can't accept their death. They perform their task to keep the afterlife calm rather than out of true compassion for a mortal's grief. Catrinas rarely visit the Universe, typically to help an extremely important mortal pass on.

Catrinas resemble skeletons dressed in bright flowers and colorful dresses, giving them a simultaneously festive and macabre appearance. Though most catrinas present as feminine, masculine catrinas still dress in bright colors and carry garlands of flowers.

Many psychopomps are intimately involved with the Boneyard's massive bureaucracy. Few pursue mercy, justice, or personal gain; their duties to Pharasma and her Boneyard are supreme. Nevertheless, individual psychopomps interpret their duties in different ways, which might put them in conflict with mortals or even with each other.

```statblock
creature: "Catrina"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
