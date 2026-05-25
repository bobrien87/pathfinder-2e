---
type: creature
group: ["Demon", "Fiend"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Kithangian"
level: "9"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Large"
trait_01: "Demon"
trait_02: "Fiend"
trait_03: "Unholy"
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+19; [[Darkvision]]"
languages: "Chthonian, Draconic, Empyrean (speak with animals, telepathy 100 feet)"
skills:
  - name: Skills
    desc: "Athletics +20, Intimidation +20, Nature +21, Stealth +16"
abilityMods: ["+6", "+3", "+5", "-2", "+4", "+3"]
abilities_top:
  - name: "Telepathy 100 feet"
    desc: "A monster with telepathy can communicate mentally with any creatures within the listed radius, as long as they share a language. This doesn't give any special access to their thoughts, and communicates no more information than normal speech would."
  - name: "Constant Spells"
    desc: "A constant spell affects the monster without the monster needing to cast it, and its duration is unlimited. If a constant spell gets counteracted, the monster can reactivate it by spending the normal spellcasting actions the spell requires."
  - name: "Animal Killer"
    desc: "A kithangian's melee Strikes deal an additional 2d6 damage to animals."
  - name: "Kithangian Venom"
    desc: "**Saving Throw** DC 25 [[Fortitude]] save <br>  <br> **Maximum Duration** 6 rounds <br>  <br> **Stage 1** 2d6 poison (2 rounds) <br>  <br> **Stage 2** 2d6 poison and [[Sickened]] 1 (2 rounds) <br>  <br> **Stage 3** 3d6 poison and [[Sickened]] 2 (2 rounds)"
armorclass:
  - name: AC
    desc: "28; **Fort** +20, **Ref** +15, **Will** +19"
health:
  - name: HP
    desc: "205; **Weaknesses** cold iron 10, holy 10"
abilities_mid:
  - name: "All-Around Vision"
    desc: "This monster can see in all directions simultaneously and therefore can't be flanked."
  - name: "+1 Status to All Saves vs. Magic"
    desc: ""
  - name: "Animal Kindness Vulnerability"
    desc: "Kithangians find kindness to animals revolting. The first time each round that a kithangian sees someone heal or otherwise provide aid to a creature that has the animal trait, the kithangian takes 3d6 mental."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Pincer +21 (`pf2:1`) (magical, reach 10 ft., unholy), **Damage** 2d12+9 slashing plus [[Grab]]"
  - name: "Melee strike"
    desc: "Stinger +21 (`pf2:1`) (agile, magical, reach 10 ft., unholy), **Damage** 2d8+9 piercing plus [[Kithangian Venom]]"
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 25, attack +17<br>**4th** [[Fly]], [[Translocate]]<br>**3rd** [[Paralyze]]<br>**2nd** [[Speak with Animals]] (Constant)<br>**1st** [[Command (At Will, Animals Only)]]"
abilities_bot:
  - name: "Change Shape"
    desc: "`pf2:1` The kithangian can take on the appearance of any Medium or Large animal. This doesn't change its Speed or their attack and damage modif ers with its Strikes, but it might change the damage type its Strikes deal. <br>  <br> The monster changes its shape indefinitely. It can use this action again to return to its natural shape or adopt a new shape. Unless otherwise noted, a monster cannot use Change Shape to appear as a specific individual. Using Change Shape counts as creating a disguise for the [[Impersonate]] use of Deception. The monster's transformation automatically defeats Perception DCs to determine whether the creature is a member of the ancestry or creature type into which it transformed, and it gains a +4 status bonus to its Deception DC to prevent others from seeing through its disguise. Change Shape abilities specify what shapes the monster can adopt. The monster doesn't gain any special abilities of the new shape, only its physical form. For example, in each shape, it replaces its normal Speeds and Strikes, and might potentially change its senses or size. Any changes are listed in its stat block."
  - name: "Rasping Tongues"
    desc: "`pf2:1` **Frequency** once per round <br>  <br> **Requirements** The kithangian has a creature [[Grabbed]] in one or both pincers <br>  <br> **Effect** Barbed tongues slither out of the faces in the kithangian's pincers. The tongues burrow into grabbed creatures and inject their minds with haunting psychic screams. Each grabbed creature takes @Damage[2d8[piercing],2d8[mental]] damage. A creature can try to resist the mental damage by attempting a DC 25 [[Will]] save."
  - name: "Grab"
    desc: "`pf2:1` **Requirements** The monster's last action was a successful Strike that lists Grab in its damage entry, or the monster has a creature [[Grabbed]] or [[Restrained]] <br>  <br> **Effect** If used after a Strike, the monster attempts to `act grapple` the creature using the body part it attacked with. This attempt neither applies nor counts toward the creature's multiple attack penalty. <br>  <br> The monster can instead use Grab and choose one creature it's grabbing or restraining with an appendage that has Grab to automatically extend that condition to the end of the monster's next turn."
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

The kithangian—a horrifying amalgam of horse and scorpion also known as a "beast demon"—is a foul fend born of the souls of mortals who abused and tormented animals in life. Kithangians tend to roam wild areas rife with animals to torture, though humanoid settlements with plenty of pets or livestock also make for tantalizing hunting grounds. Uncontested for too long, a kithangian's presence has a corrupting influence on the local fauna, which birth fiendish monstrosities until the demon is vanquished. If it realizes it's being tracked by vengeful druids or demon slayers, a kithangian assumes the shape of an unassuming animal so it can get the jump on its pursuers.

```statblock
creature: "Kithangian"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
