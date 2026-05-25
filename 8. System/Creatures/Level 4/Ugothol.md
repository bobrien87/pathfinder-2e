---
type: creature
group: ["Aberration"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Ugothol"
level: "4"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Medium"
trait_01: "Aberration"
trait_02: ""
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+10; [[Darkvision]]"
languages: "Alghollthu, Common, Thalassic (Truespeech)"
skills:
  - name: Skills
    desc: "Acrobatics +12, Athletics +12, Deception +13, Stealth +13, Thievery +9"
abilityMods: ["+4", "+3", "+3", "+0", "+2", "+3"]
abilities_top:
  - name: "Constant Spells"
    desc: "A constant spell affects the monster without the monster needing to cast it, and its duration is unlimited. If a constant spell gets counteracted, the monster can reactivate it by spending the normal spellcasting actions the spell requires."
  - name: "Assume Form"
    desc: "The ugothol spends 10 minutes reshaping its appearance to take on the shape of any Small or Medium humanoid. It gains a +4 circumstance bonus to Deception checks to pass as that creature."
  - name: "Compression"
    desc: "When the ugothol successfully [[Squeezes]], it moves through the tight space at full speed. Narrow confines are not difficult terrain for an ugothol."
  - name: "Sneak Attack"
    desc: "The ugothol deals 1d6 extra precision damage to [[Off Guard]] creatures."
armorclass:
  - name: AC
    desc: "21; **Fort** +9, **Ref** +9, **Will** +12"
health:
  - name: HP
    desc: "60; **Resistances** bludgeoning 5"
abilities_mid:
  - name: "+2 Status to All Saves vs. Auditory and Visual"
    desc: ""
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Longsword +14 (`pf2:1`) (versatile p), **Damage** 1d8+6 slashing"
  - name: "Melee strike"
    desc: "Claw +12 (`pf2:1`) (agile, unarmed), **Damage** 2d6+6 slashing plus [[Grab]]"
spellcasting:
  - name: "Occult Innate Spells"
    desc: "DC 19, attack +11<br>**5th** [[Truespeech]] (Constant)"
abilities_bot:
  - name: "Blood Nourishment"
    desc: "`pf2:1` The ugothol uses its three-pronged tongue to drink the blood of an adjacent [[Restrained]] or [[Unconscious]] creature. The creature gains [[Drained]] 1"
  - name: "Revert Form"
    desc: "`pf2:0` **Requirements** The ugothol is in an assumed form <br>  <br> **Effect** The ugothol resumes its true form. Until the start of its next turn, it gains a +2 status bonus to attack rolls, damage rolls, saving throws, and skill checks. <br>  <br> > [!danger] Effect: Revert Form"
  - name: "Grab"
    desc: "`pf2:1` **Requirements** The monster's last action was a successful Strike that lists Grab in its damage entry, or the monster has a creature [[Grabbed]] or [[Restrained]] <br>  <br> **Effect** If used after a Strike, the monster attempts to `act grapple` the creature using the body part it attacked with. This attempt neither applies nor counts toward the creature's multiple attack penalty. <br>  <br> The monster can instead use Grab and choose one creature it's grabbing or restraining with an appendage that has Grab to automatically extend that condition to the end of the monster's next turn."
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

Among the subtler of the alghollthu creations were the ugothols—also known as faceless stalkers. These twisted beings used shapeshifting to infiltrate settlements and assassinate key targets. They sowed discord and replaced leaders, causing unwanted organizations to implode and bothersome people to lose face and eventually disappear.

In bygone millennia, aquatic monsters known as alghollthus used their occult powers to conquer and rule vast swaths of the world. Alghollthus shaped their servitors and other creatures using mental manipulation and physically transformative magic. The rulers of the alghollthus, the so-called "veiled masters," further shaped entire societies by assuming the forms of those they controlled.

In time, the alghollthus grew frustrated with upstart surface societies and meddling gods. They used incredible magical power to call forth a cataclysm, hoping to destroy the rebellious societies they'd manipulated. Yet they miscalculated the will to survive of those they treated as their pawns, and in time the world recovered, this time free of alghollthu influence.

Today, the alghollthus have mostly remained within the deep aquatic realms where they still rule without question. Yet they have not abandoned their plots entirely, and the reemergence of servitors like faceless stalkers suggests that the alghollthus have turned their hateful eyes to the surface once again.

```statblock
creature: "Ugothol"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
