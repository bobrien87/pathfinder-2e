---
type: creature
group: ["Monitor", "Psychopomp"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Eseneth"
level: "17"
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
    desc: "+29; [[Darkvision]], [[Lifesense]] (precise) 120 feet"
languages: "Chthonian, Diabolic, Empyrean, Requian"
skills:
  - name: Skills
    desc: "Acrobatics +33, Athletics +33, Medicine +31, Stealth +33, Boneyard Lore +29, Sewing Lore +35"
abilityMods: ["+8", "+8", "+5", "+6", "+4", "+2"]
abilities_top:
  - name: "Constant Spells"
    desc: "A constant spell affects the monster without the monster needing to cast it, and its duration is unlimited. If a constant spell gets counteracted, the monster can reactivate it by spending the normal spellcasting actions the spell requires."
  - name: "Shepherd's Touch"
    desc: "A eseneth's Strikes affect incorporeal creatures with the effects of a *[[Ghost Touch]]* property rune and deal 2d6 void damage to living creatures and 2d6 vitality damage to undead."
  - name: "Spirit Grasp"
    desc: "An eseneth can [[Grapple]] incorporeal creatures despite being corporeal. The eseneth uses Athletics to Grapple incorporeal creatures as normal but can't use Athletics for other actions against incorporeal creatures, like [[Shove]] or [[Trip]]."
armorclass:
  - name: AC
    desc: "39; **Fort** +28, **Ref** +32, **Will** +27"
health:
  - name: HP
    desc: "290; **Immunities** death effects, disease; **Resistances** poison 15, void 15"
abilities_mid:
  - name: "Improved Grab"
    desc: "`pf2:0` **Trigger** The monster's last action was a successful Strike that lists Improved Grab in its damage entry, or the monster has a creature [[Grabbed]] or [[Restrained]] <br>  <br> **Effect** If used after a Strike, the monster attempts to `act grapple` the creature using the body part it attacked with as a free action. This attempt neither applies nor counts toward the creature's multiple attack penalty. <br>  <br> The monster can instead use Improved Grab as an action and choose one creature it's grabbing or restraining with an appendage that has Improved Grab to automatically extend that condition to the end of the monster's next turn."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Spirit Needle +33 (`pf2:1`) (magical), **Damage** 3d10+14 piercing plus [[Improved Grab]] plus [[Shepherds Touch]]"
  - name: "Melee strike"
    desc: "Spirit Needle +33 (`pf2:1`) (magical, thrown 30), **Damage** 3d10+14 piercing plus [[Shepherds Touch]]"
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 38, attack +30<br>**6th** [[Spirit Blast]]<br>**4th** [[Translocate]] (At Will), [[Unfettered Movement]] (Constant)<br>**2nd** [[Invisibility (At will, Self Only)]]"
abilities_bot:
  - name: "Mend Soul"
    desc: "`pf2:1` **Frequency** once per round <br>  <br> **Effect** The eseneth restores 25 healing HP to itself or an incorporeal creature it has [[Grabbed]]."
  - name: "Seize Soul"
    desc: "`pf2:1` **Requirements** The eseneth has a corporeal creature [[Grabbed]] or [[Restrained]] <br>  <br> **Effect** The eseneth tries to yank the soul out of the required creature. The eseneth attempts an Athletics check against the target's Fortitude DC. <br> - **Critical Success** The eseneth grabs the target's soul. The body is released and is [[Paralyzed]] for 2 rounds. When the body ceases being paralyzed, its soul returns instantly, and the target wakes. The soul—grabbed by the eseneth—is incorporeal, is [[Invisible]], has a fly Speed equal to the creature's Speed, and otherwise has all the same statistics. It can't attack, cast spells, or attempt any skill checks that require a physical body other than checks to [[Escape]] (DC 38), and it must always maintain line of effect to its body. <br> - **Success** As critical success, but the paralysis ends after 1 round. <br> - **Failure** The target remains grabbed or restrained, but its soul remains in its body. <br> - **Critical Failure** The target is no longer grabbed or restrained."
  - name: "Shred Soul"
    desc: "`pf2:1` **Frequency** once per round <br>  <br> **Requirements** The eseneth has an incorporeal creature [[Grabbed]] or [[Restrained]] <br>  <br> **Effect** The eseneth deals @Damage[(3d10+14)[force]] damage to the required creature."
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

Eseneths, commonly known as soul-stitchers, are dispassionate surgeons who repair damaged souls. They operate with professional efficiency, manifesting large stitching needles composed of spirit energy to do their necessary work. An eseneth appears as a slim, hairless, gray-skinned humanoid with no facial features. Patches of dark, raised flesh dot their upper chest and shoulders.

Many psychopomps are intimately involved with the Boneyard's massive bureaucracy. Few pursue mercy, justice, or personal gain; their duties to Pharasma and her Boneyard are supreme. Nevertheless, individual psychopomps interpret their duties in different ways, which might put them in conflict with mortals or even with each other.

```statblock
creature: "Eseneth"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
