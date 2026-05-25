---
type: creature
group: ["Monitor", "Protean"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Izfiitar"
level: "20"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Medium"
trait_01: "Monitor"
trait_02: "Protean"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+36; [[Darkvision]]"
languages: "Chthonian, Empyrean, Protean (Telepathy 100 feet, Truespeech)"
skills:
  - name: Skills
    desc: "Acrobatics +38, Arcana +35, Athletics +35, Deception +37, Diplomacy +37, Occultism +36, Religion +38, Society +35, Stealth +38, Maelstrom Lore +37"
abilityMods: ["+9", "+10", "+9", "+7", "+8", "+9"]
abilities_top:
  - name: "Telepathy 100 feet"
    desc: "A monster with telepathy can communicate mentally with any creatures within the listed radius, as long as they share a language. This doesn't give any special access to their thoughts, and communicates no more information than normal speech would."
  - name: "Entropy Sense (Imprecise) 120 feet"
    desc: "A Izfiitar can anticipate the most likely location of a creature through their supernatural insight into the forces of chaotic probabilities and chance. This grants the izflitar the ability to sense creatures within the listed range. <br>  <br> The izflitar's entropy sense doesn't detect creatures under the effects of [[Veil of Privacy]] or that are otherwise shielded from divinations and predictions."
  - name: "Constant Spells"
    desc: "A constant spell affects the monster without the monster needing to cast it, and its duration is unlimited. If a constant spell gets counteracted, the monster can reactivate it by spending the normal spellcasting actions the spell requires."
  - name: "Greater Warpwave Strike"
    desc: "Any creature struck and damaged by an izfiitar's jaws or claw Strike must succeed at a DC 42 [[Fortitude]] save or be subject to a particularly powerful Warpwave. <br>  <br> Roll twice and apply both affects, rerolling any duplicates."
  - name: "Reshape Reality"
    desc: "When the izfiitar casts [[Mirage]], it infuses the illusion with quasi-real substance. Creatures that don't disbelieve the illusion treat structures and terrain created through the spell as though they were real, ascending illusory stairs, becoming trapped by illusory quicksand, and so on."
armorclass:
  - name: AC
    desc: "44; **Fort** +33, **Ref** +36, **Will** +38"
health:
  - name: HP
    desc: "360; fast healing 20; **Resistances** acid 20, precision 20, protean anatomy 25"
abilities_mid:
  - name: "+1 Status to All Saves vs. Magic"
    desc: ""
  - name: "Fast Healing 20"
    desc: "A monster with this ability regains the given number of Hit Points each round at the beginning of its turn."
  - name: "Kiss of the Speakers"
    desc: "The izfiitar continuously tinkers with the myriad possibilities in which it can move or manipulate magic. The izfiitar is always [[Quickened]] and can use the extra action only to Step, Stride, or as part of Casting a Spell."
  - name: "Prescient Revision"
    desc: "`pf2:r` **Trigger** The izfiitar fails a check <br>  <br> **Effect** The izfiitar rerolls the triggering check and takes the better result. For 1d4 rounds, it loses the effects of Kiss of the Speakers and can't use Reshape Reality."
  - name: "Protean Anatomy 25"
    desc: "A izfiitar's vital organs shift and change shape and position constantly. Immediately after the izfiitar takes acid, electricity, or sonic damage, it gains the listed amount of resistance to that damage type. This lasts for 1 hour or until the next time the protean takes damage of one of the other types (in which case its resistance changes to match that type), whichever comes first. <br>  <br> The izfiitar is immune to polymorph effects unless it is a willing target. If [[Blinded]] or [[Deafened]], the izfiitar automatically recovers at the end of its next turn as new sensory organs grow to replace the compromised ones. <br>  <br> > [!danger] Effect: Protean Anatomy"
  - name: "Improved Grab"
    desc: "`pf2:0` **Trigger** The monster's last action was a successful Strike that lists Improved Grab in its damage entry, or the monster has a creature [[Grabbed]] or [[Restrained]] <br>  <br> **Effect** If used after a Strike, the monster attempts to `act grapple` the creature using the body part it attacked with as a free action. This attempt neither applies nor counts toward the creature's multiple attack penalty. <br>  <br> The monster can instead use Improved Grab as an action and choose one creature it's grabbing or restraining with an appendage that has Improved Grab to automatically extend that condition to the end of the monster's next turn."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Jaws +38 (`pf2:1`) (finesse, magical), **Damage** 4d10+19 piercing plus [[Greater Warpwave Strike]]"
  - name: "Melee strike"
    desc: "Claw +38 (`pf2:1`) (agile, finesse, magical), **Damage** 4d8+19 slashing plus [[Greater Warpwave Strike]]"
  - name: "Melee strike"
    desc: "Tail +38 (`pf2:1`) (magical, reach 10 ft.), **Damage** 4d12+19 bludgeoning plus [[Improved Grab]]"
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 47, attack +39<br>**10th** [[Manifestation]]<br>**9th** [[Massacre]], [[Overwhelming Presence]]<br>**7th** [[Warp Mind]] (At Will)<br>**6th** [[Cursed Metamorphosis]], [[Disintegrate]], [[Teleport (At Will, Self Only)]]<br>**5th** [[Truespeech]] (Constant)<br>**4th** [[Confusion]], [[Creation]] (At Will), [[Divine Wrath]], [[Mirage (At Will, See Reshape Reality)]], [[Translocate]], [[Translocate]] (At Will), [[Unfettered Movement]] (Constant)<br>**2nd** [[Dispel Magic]]"
abilities_bot:
  - name: "Change Shape"
    desc: "`pf2:1` The izfiitar takes the appearance of any Huge or smaller creature. This doesn't change its Speed or its attack and damage bonuses with its Strikes, but might change the damage type its Strikes deal. <br>  <br> The monster changes its shape indefinitely. It can use this action again to return to its natural shape or adopt a new shape. Unless otherwise noted, a monster cannot use Change Shape to appear as a specific individual. Using Change Shape counts as creating a disguise for the [[Impersonate]] use of Deception. The monster's transformation automatically defeats Perception DCs to determine whether the creature is a member of the ancestry or creature type into which it transformed, and it gains a +4 status bonus to its Deception DC to prevent others from seeing through its disguise. Change Shape abilities specify what shapes the monster can adopt. The monster doesn't gain any special abilities of the new shape, only its physical form. For example, in each shape, it replaces its normal Speeds and Strikes, and might potentially change its senses or size. Any changes are listed in its stat block."
  - name: "Constrict"
    desc: "`pf2:1` @Damage[(2d8+17)[bludgeoning]] damage, DC 44 [[Fortitude]] save <br>  <br> The monster deals the listed amount of damage to any number of creatures [[Grabbed]] or [[Restrained]] by it. Each of those creatures can attempt a basic Fortitude save with the listed DC."
  - name: "Storm of Claws"
    desc: "`pf2:2` The izfiitar makes up to six claw Strikes, each against a different target."
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

Occupying the pinnacle of the loose protean caste system, izfiitars enact the ever-shifting plans of the vaunted protean lords and those of the divine Speakers of the Depths.

Proteans are manifestations of chaos made flesh, natives of the Maelstrom that embody the primeval potency of entropy in their serpentine forms.

```statblock
creature: "Izfiitar"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
