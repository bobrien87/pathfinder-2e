---
type: creature
group: ["Monitor", "Protean"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Imentesh"
level: "10"
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
    desc: "+19; [[Darkvision]]"
languages: "Chthonian, Empyrean, Protean (Truespeech)"
skills:
  - name: Skills
    desc: "Acrobatics +17, Athletics +19, Deception +21, Diplomacy +19, Performance +21, Stealth +21, Thievery +17"
abilityMods: ["+7", "+5", "+5", "+7", "+3", "+5"]
abilities_top:
  - name: "Entropy Sense"
    desc: "An imentesh can anticipate the most likely location of a creature through their supernatural insight into the forces of chaotic probabilities and chance. This grants the imentesh the ability to sense creatures within the listed range. A creature under the effects of [[Veil of Privacy]] or that is otherwise shielded from divination and prediction cannot be noticed via entropy sense."
  - name: "Constant Spells"
    desc: "A constant spell affects the monster without the monster needing to cast it, and its duration is unlimited. If a constant spell gets counteracted, the monster can reactivate it by spending the normal spellcasting actions the spell requires."
  - name: "Sneak Attack"
    desc: "An imentesh's Strikes deal an additional 2d6 precision damage to [[Off Guard]] targets."
  - name: "Warpwave Strike"
    desc: "Any creature struck and damaged by an imentesh's jaws Strike must succeed at a DC 29 [[Fortitude]] save or be subject to a warpwave."
  - name: "Warpwaves"
    desc: "Many proteans can subject their foes to disorienting alterations perceived in time and space by creating ripples of unstable reality in the environment called warpwaves. <br>  <br> When a creature fails its saving throw and is affected by a warpwave, roll `r 1d8` and consult the table below for the specific effect on that creature. <br>  <br> Unless indicated otherwise, a warpwave effect lasts for 1d4 rounds, and a new warpwave effect negates any previous warpwave effect already affecting a creature. <br>  <br> d8 <br> Warpwave Effect <br>  <br> 1 <br> [[Clumsy]] 2 ([[Clumsy]] 3 on a critical failure) <br>  <br> 2 <br> [[Confused]] and gains 4d6 temporary Hit Points <br>  <br> 3 <br> [[Dazzled]] (permanent on a critical failure) <br>  <br> 4 <br> [[Enfeebled]] 2 ([[Enfeebled]] 3 on a critical failure) <br>  <br> 5 <br> [[Immobilized]] by filaments of energy <br>  <br> 6 <br> [[Quickened]] (Stride, Strike, or Step only) <br>  <br> 7 <br> [[Slowed]] 1 <br>  <br> 8 <br> [[Stupefied 2]] ([[Stupefied 3]] on a critical failure)"
armorclass:
  - name: AC
    desc: "30; **Fort** +21, **Ref** +19, **Will** +17"
health:
  - name: HP
    desc: "175; fast healing 5; **Resistances** precision 10, protean anatomy 15"
abilities_mid:
  - name: "+1 Status to All Saves vs. Magic"
    desc: ""
  - name: "Fast Healing 5"
    desc: "A monster with this ability regains the given number of Hit Points each round at the beginning of its turn."
  - name: "Protean Anatomy 15"
    desc: "An imentesh's vital organs shift and change shape and position constantly. Immediately after the imentesh takes acid, electricity, or sonic damage, it gains the listed amount of resistance to that damage type. This lasts for 1 hour or until the next time the protean takes damage of one of the other types (in which case its resistance changes to match that type), whichever comes first. <br>  <br> The imentesh is immune to polymorph effects unless it is a willing target. If [[Blinded]] or [[Deafened]], the imentesh automatically recovers at the end of its next turn as new sensory organs grow to replace the compromised ones. <br>  <br> > [!danger] Effect: Protean Anatomy"
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Jaws +23 (`pf2:1`) (magical, reach 10 ft.), **Damage** 2d10+11 piercing plus [[Warpwave Strike]]"
  - name: "Melee strike"
    desc: "Claw +23 (`pf2:1`) (agile, magical, reach 10 ft.), **Damage** 2d6+11 slashing"
  - name: "Melee strike"
    desc: "Tail +23 (`pf2:1`) (magical, reach 15 ft.), **Damage** 2d10+11 bludgeoning plus 1d6 spirit plus [[Grab]]"
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 29, attack +21<br>**5th** [[Sending]], [[Truespeech]] (Constant)<br>**4th** [[Creation]], [[Translocate]], [[Translocate]] (At Will), [[Unfettered Movement]] (Constant)<br>**3rd** [[Crisis of Faith]], [[Haste]], [[Shrink Item]], [[Slow]]<br>**2nd** [[Dispel Magic]], [[Shatter]]<br>**1st** [[Mending]]"
abilities_bot:
  - name: "Change Shape"
    desc: "`pf2:1` The imentesh takes the appearance of any Large or smaller creature. This doesn't change its Speed or its attack and damage bonuses with its Strikes, but might change the damage type its Strikes deal. <br>  <br> The monster changes its shape indefinitely. It can use this action again to return to its natural shape or adopt a new shape. Unless otherwise noted, a monster cannot use Change Shape to appear as a specific individual. Using Change Shape counts as creating a disguise for the [[Impersonate]] use of Deception. The monster's transformation automatically defeats Perception DCs to determine whether the creature is a member of the ancestry or creature type into which it transformed, and it gains a +4 status bonus to its Deception DC to prevent others from seeing through its disguise. Change Shape abilities specify what shapes the monster can adopt. The monster doesn't gain any special abilities of the new shape, only its physical form. For example, in each shape, it replaces its normal Speeds and Strikes, and might potentially change its senses or size. Any changes are listed in its stat block."
  - name: "Constrict"
    desc: "`pf2:1` @Damage[(1d10+11)[bludgeoning]] damage, DC 29 [[Fortitude]] save <br>  <br> The monster deals the listed amount of damage to any number of creatures [[Grabbed]] or [[Restrained]] by it. Each of those creatures can attempt a basic Fortitude save with the listed DC."
  - name: "Inflict Warpwave"
    desc: "`pf2:1` An imentesh inflicts a warpwave on a creature within 100 feet (DC 29 [[Fortitude]] save to resist)."
  - name: "Grab"
    desc: "`pf2:1` **Requirements** The monster's last action was a successful Strike that lists Grab in its damage entry, or the monster has a creature [[Grabbed]] or [[Restrained]] <br>  <br> **Effect** If used after a Strike, the monster attempts to `act grapple` the creature using the body part it attacked with. This attempt neither applies nor counts toward the creature's multiple attack penalty. <br>  <br> The monster can instead use Grab and choose one creature it's grabbing or restraining with an appendage that has Grab to automatically extend that condition to the end of the monster's next turn."
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

The loquacious proteans known as imenteshes serve as missionaries, spies, and heralds of chaos to further the protean goal of reality's dissolution.

Proteans are manifestations of chaos made flesh, natives of the Maelstrom that embody the primeval potency of entropy in their serpentine forms.

```statblock
creature: "Imentesh"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
