---
type: creature
group: ["Monitor", "Protean"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Naunet"
level: "7"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Large"
trait_01: "Monitor"
trait_02: "Protean"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+14; [[Darkvision]]"
languages: "Chthonian, Empyrean, Protean"
skills:
  - name: Skills
    desc: "Acrobatics +14, Athletics +16, Intimidation +16, Stealth +14, Survival +12"
abilityMods: ["+5", "+3", "+5", "+0", "+3", "+3"]
abilities_top:
  - name: "Entropy Sense (Imprecise) 30 feet"
    desc: "A naunet can anticipate the most likely presence of a creature through a supernatural insight into chaotic probabilities and chance. This grants them the ability to sense creatures within the listed range. Veil of privacy prevents a creature from being detected via entropy sense automatically (without a counteract check)."
  - name: "Constant Spells"
    desc: "A constant spell affects the monster without the monster needing to cast it, and its duration is unlimited. If a constant spell gets counteracted, the monster can reactivate it by spending the normal spellcasting actions the spell requires."
  - name: "Confounding Slam"
    desc: "A creature hit by the naunet's tentacle Strike is [[Stupefied 2]] for 1d4 rounds (DC 25 [[Will]] save negates). If the creature was already stupefied in this way, the duration extends by 1 round instead."
armorclass:
  - name: AC
    desc: "24; **Fort** +18, **Ref** +14, **Will** +12"
health:
  - name: HP
    desc: "120; **Resistances** precision 5, protean anatomy 10"
abilities_mid:
  - name: "+1 Status to All Saves vs. Magic"
    desc: ""
  - name: "Fast Healing 2"
    desc: "A monster with this ability regains the given number of Hit Points each round at the beginning of its turn."
  - name: "Protean Anatomy 10"
    desc: "A protean's vital organs shift and change shape and position constantly. Immediately after the protean takes acid, electricity, or sonic damage, it gains the listed amount of resistance to that damage type. This lasts for 1 hour or until the next time the protean takes damage of one of the other types (in which case its resistance changes to match that type), whichever comes first. The protean is immune to polymorph effects unless it is a willing target. If [[Blinded]] or [[Deafened]], the protean automatically recovers at the end of its next turn as new sensory organs grow to replace the compromised ones. <br>  <br> > [!danger] Effect: Protean Anatomy"
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Jaws +18 (`pf2:1`) (magical, reach 10 ft.), **Damage** 2d10+8 piercing"
  - name: "Melee strike"
    desc: "Tail +18 (`pf2:1`) (magical, reach 15 ft.), **Damage** 2d8+8 bludgeoning plus [[Grab]]"
  - name: "Melee strike"
    desc: "Tentacle +18 (`pf2:1`) (agile, magical, reach 10 ft., unarmed), **Damage** 2d8+8 piercing"
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 25, attack +17<br>**4th** [[Translocate]], [[Unfettered Movement]] (Constant)<br>**3rd** [[Vampiric Feast]]<br>**2nd** [[Acid Grip]], [[Mist]] (At Will), [[Shatter]] (At Will)"
abilities_bot:
  - name: "Adaptive Strike"
    desc: "`pf2:0` The naunet chooses adamantine, cold iron, or silver; its melee Strikes count as that type for 1 minute or until it uses Adaptive Strike again. <br>  <br> > [!danger] Effect: Adaptive Strike"
  - name: "Change Shape"
    desc: "`pf2:1` The naunet can take the appearance of any Small, Medium, or Large animal, beast, or humanoid. This doesn't change its Speed or its attack and damage bonuses with its Strikes but might change the damage type its Strikes deal. <br>  <br> The monster changes its shape indefinitely. It can use this action again to return to its natural shape or adopt a new shape. Unless otherwise noted, a monster cannot use Change Shape to appear as a specific individual. Using Change Shape counts as creating a disguise for the [[Impersonate]] use of Deception. The monster's transformation automatically defeats Perception DCs to determine whether the creature is a member of the ancestry or creature type into which it transformed, and it gains a +4 status bonus to its Deception DC to prevent others from seeing through its disguise. Change Shape abilities specify what shapes the monster can adopt. The monster doesn't gain any special abilities of the new shape, only its physical form. For example, in each shape, it replaces its normal Speeds and Strikes, and might potentially change its senses or size. Any changes are listed in its stat block."
  - name: "Constrict"
    desc: "`pf2:1` @Damage[(1d8+8)[bludgeoning]] damage, DC 22 [[Fortitude]] save <br>  <br> The monster deals the listed amount of damage to any number of creatures [[Grabbed]] or [[Restrained]] by it. Each of those creatures can attempt a basic Fortitude save with the listed DC."
  - name: "Grab"
    desc: "`pf2:1` **Requirements** The monster's last action was a successful Strike that lists Grab in its damage entry, or the monster has a creature [[Grabbed]] or [[Restrained]] <br>  <br> **Effect** If used after a Strike, the monster attempts to `act grapple` the creature using the body part it attacked with. This attempt neither applies nor counts toward the creature's multiple attack penalty. <br>  <br> The monster can instead use Grab and choose one creature it's grabbing or restraining with an appendage that has Grab to automatically extend that condition to the end of the monster's next turn."
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

Pugnacious and powerfully muscled, naunets serve as the scouts and rank-and-file troops of protean armies.

Proteans are manifestations of chaos made flesh, natives of the Maelstrom that embody the primeval potency of entropy in their serpentine forms.

```statblock
creature: "Naunet"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
