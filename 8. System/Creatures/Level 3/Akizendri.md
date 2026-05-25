---
type: creature
group: ["Monitor", "Protean"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Akizendri"
level: "3"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Small"
trait_01: "Monitor"
trait_02: "Protean"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+8; [[Darkvision]]"
languages: "Chthonian, Empyrean, Protean (Telepathy touch only)"
skills:
  - name: Skills
    desc: "Acrobatics +9, Athletics +9, Deception +10, Occultism +11, Society +10, Stealth +9, Thievery +9"
abilityMods: ["+3", "+4", "+1", "+4", "+3", "+1"]
abilities_top:
  - name: "Telepathy (Touch Only)"
    desc: "A monster with telepathy can communicate mentally with any creatures within the listed radius, as long as they share a language. This doesn't give any special access to their thoughts, and communicates no more information than normal speech would."
  - name: "Entropy Sense (Imprecise) 30 feet"
    desc: "An akizendri can anticipate the most likely presence of a creature through a supernatural insight into chaotic probabilities and chance. This grants them the ability to sense creatures within the listed range. [[Veil of Privacy]] prevents a creature from being detected via entropy sense automatically (without a counteract check)."
  - name: "Constant Spells"
    desc: "A constant spell affects the monster without the monster needing to cast it, and its duration is unlimited. If a constant spell gets counteracted, the monster can reactivate it by spending the normal spellcasting actions the spell requires."
  - name: "Garbled Thoughts"
    desc: "A creature hit by the akizendri's bite Strike must attempt a DC 20 [[Will]] save. <br> - **Success** The creature is unaffected. <br> - **Failure** The creature is [[Stupefied 1]] for 1d4 rounds. <br> - **Critical Failure** As failure, but the creature is also [[Confused]] for 1 round."
  - name: "Text Immersion"
    desc: "As a 1-minute activity, the akizendri physically immerses itself in a page of text it's touching, changing the message of the text in the process. It can exit the book at any point by Dismissing this ability, at which point it appears in a space adjacent to the text. If it does so to begin combat, it rolls a Deception check for initiative. As long as it remains immersed in the text, the akizendri has no body. It can communicate telepathically with a creature as long as the creature touches the book or scroll that contains it. It can sense nearby creatures using its entropy sense, but not in any other way, nor can it use any attack, manipulate, or move actions or speak aloud. If the object it's immersed in is destroyed, the akizendri reappears in an adjacent square and is [[Stunned]] 1."
armorclass:
  - name: AC
    desc: "19; **Fort** +6, **Ref** +11, **Will** +10"
health:
  - name: HP
    desc: "40; fast healing 1; **Resistances** precision 3, protean anatomy 6"
abilities_mid:
  - name: "Fast Healing 1"
    desc: "A monster with this ability regains the given number of Hit Points each round at the beginning of its turn."
  - name: "Protean Anatomy"
    desc: "An akizendri's vital organs shift and change shape and position constantly. Immediately after the akizendri takes acid, electricity, or sonic damage, they gain the listed amount of resistance to that damage type. This lasts for 1 hour or until the next time the protean takes damage of one of the other types (in which case their resistance changes to match that type), whichever comes first. <br>  <br> The akizendri is immune to polymorph effects unless they're a willing target. If [[Blinded]] or [[Deafened]], the akizendri automatically recovers at the end of their next turn as new sensory organs grow to replace the compromised ones. <br>  <br> > [!danger] Effect: Protean Anatomy"
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Jaws +12 (`pf2:1`) (finesse, magical), **Damage** 2d8+3 piercing plus 1d4 spirit plus [[Garbled Thoughts]]"
  - name: "Melee strike"
    desc: "Tail +12 (`pf2:1`) (finesse, magical), **Damage** 2d6+3 bludgeoning plus 1d4 spirit plus [[Grab]]"
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 20, attack +12<br>**4th** [[Unfettered Movement]] (Constant)<br>**2nd** [[Dispel Magic]]<br>**1st** [[Caustic Blast]], [[Daze]], [[Figment]], [[Sigil]], [[Telekinetic Hand]]"
abilities_bot:
  - name: "Change Shape"
    desc: "`pf2:1` The akizendri takes on the appearance of any Small or smaller creature. This doesn't change its Speed or its attack and damage bonuses with its Strikes, but might change the damage type its Strikes deal. <br>  <br> The monster changes its shape indefinitely. It can use this action again to return to its natural shape or adopt a new shape. Unless otherwise noted, a monster cannot use Change Shape to appear as a specific individual. Using Change Shape counts as creating a disguise for the [[Impersonate]] use of Deception. The monster's transformation automatically defeats Perception DCs to determine whether the creature is a member of the ancestry or creature type into which it transformed, and it gains a +4 status bonus to its Deception DC to prevent others from seeing through its disguise. Change Shape abilities specify what shapes the monster can adopt. The monster doesn't gain any special abilities of the new shape, only its physical form. For example, in each shape, it replaces its normal Speeds and Strikes, and might potentially change its senses or size. Any changes are listed in its stat block."
  - name: "Constrict"
    desc: "`pf2:1` @Damage[(1d8+3)[bludgeoning]] damage, DC 20 [[Fortitude]] save <br>  <br> The monster deals the listed amount of damage to any number of creatures [[Grabbed]] or [[Restrained]] by it. Each of those creatures can attempt a basic Fortitude save with the listed DC."
  - name: "Grab"
    desc: "`pf2:1` **Requirements** The monster's last action was a successful Strike that lists Grab in its damage entry, or the monster has a creature [[Grabbed]] or [[Restrained]] <br>  <br> **Effect** If used after a Strike, the monster attempts to `act grapple` the creature using the body part it attacked with. This attempt neither applies nor counts toward the creature's multiple attack penalty. <br>  <br> The monster can instead use Grab and choose one creature it's grabbing or restraining with an appendage that has Grab to automatically extend that condition to the end of the monster's next turn."
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

Akizendris gnaw at sources of knowledge and lore, gleefully corrupting and altering them to vex scholars across the planes with contradictions and untruths.

Proteans are manifestations of chaos made flesh, natives of the Maelstrom that embody the primeval potency of entropy in their serpentine forms.

```statblock
creature: "Akizendri"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
