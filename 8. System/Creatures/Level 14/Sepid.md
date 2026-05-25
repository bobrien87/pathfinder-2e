---
type: creature
group: ["Div", "Fiend"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Sepid"
level: "14"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Large"
trait_01: "Div"
trait_02: "Fiend"
trait_03: "Unholy"
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+24; [[Greater Darkvision]]"
languages: "Common, Daemonic (telepathy 100 feet)"
skills:
  - name: Skills
    desc: "Acrobatics +23, Arcana +20, Athletics +28, Deception +22, Intimidation +26, Religion +20, Stealth +23"
abilityMods: ["+8", "+5", "+8", "+4", "+4", "+6"]
abilities_top:
  - name: "Telepathy 100 feet"
    desc: "A monster with telepathy can communicate mentally with any creatures within the listed radius, as long as they share a language. This doesn't give any special access to their thoughts, and communicates no more information than normal speech would."
armorclass:
  - name: AC
    desc: "34; **Fort** +28, **Ref** +23, **Will** +20"
health:
  - name: HP
    desc: "350; **Weaknesses** cold iron 10, holy 10"
abilities_mid:
  - name: "+1 Status to All Saves vs. Magic"
    desc: ""
  - name: "Blatant Liar"
    desc: "While all divs delight in lying, sepids are compulsive and predictable liars who always do the opposite of what they claim they'll do. If a sepid is ever forced or compelled to tell the truth, they take 4d8 mental damage."
  - name: "Deflecting Lie"
    desc: "`pf2:r` **Trigger** A creature hits the sepid with a ranged Strike or a ranged spell attack roll <br>  <br> **Effect** The sepid lies in an attempt to divert the attack. They roll a [[Deception]] check against the triggering creature's Perception DC. On a success, if the triggering attack roll was a success, it becomes a failure, and if the triggering attack roll was a critical hit, it becomes a normal success."
  - name: "Reactive Strike"
    desc: "`pf2:r` A sepid gains an extra reaction each round that they can use only to make a Reactive Strike. <br>  <br> **Trigger** A creature within the monster's reach uses a manipulate action or a move action, makes a ranged attack, or leaves a square during a move action it's using. <br>  <br> **Effect** The monster attempts a melee Strike against the triggering creature. If the attack is a critical hit and the trigger was a manipulate action, the monster disrupts that action. This Strike doesn't count toward the monster's multiple attack penalty, and its multiple attack penalty doesn't apply to this Strike."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Falchion +30 (`pf2:1`) (forceful, magical, sweep, unholy), **Damage** 2d10+16 slashing plus 1d6 mental"
  - name: "Melee strike"
    desc: "Claw +28 (`pf2:1`) (agile, magical, unarmed, unholy), **Damage** 3d6+16 slashing plus 1d6 mental"
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 34, attack +26<br>**4th** [[Fly]], [[Translocate]] (At Will)<br>**3rd** [[Paralyze]], [[Veil of Privacy (at will; self only)]]<br>**2nd** [[Darkness]] (At Will), [[Dispel Magic]], [[Translate (at will; self only)]]<br>**1st** [[Detect Magic]]"
abilities_bot:
  - name: "Rain of Debris"
    desc: "`pf2:2` The sepid calls forth a hail of stone, wood, metal, and similar debris in a @Template[emanation|distance:40], dealing @Damage[10d6[bludgeoning],5d6[spirit]|options:area-damage]{10d6 bludgeoning damage and 5d6 spirit damage}. Each creature in the area other than the sepid must attempt a DC 31 [[Reflex]] save saving throw. <br>  <br> The sepid can't use Rain of Debris again for 1d4 rounds."
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

Sepids are the brutal warlords of the divs, delighting in violence against mortals and their own particular flavor of vengeance. Inveterate liars, sepids can't help but spout the most outrageous lies, and their form and nature represent the power of falsehoods to snowball into violence that can cost countless lives. Among mortals, they rally troops to incite rebellion, war, and other form of carnage, savoring mortals who slaughter each other. These giant beings usually stand around 13 feet tall; they wade through battlefields seeking out heroes and generals, rejoicing maniacally as they cut their foes down.

Some fiends want to tear down the multiverse; others dedicate themselves to creating chaos and carnage, or to rule over realms with an iron fist. Divs strive toward a different, if equally reprehensible, goal-they seek to thwart and ruin the schemes and works of mortal beings.

Long ago, divs were once genies bound to serve ancient mortal empires lost to the passage of eons. In the beginning, these genies were masters of creation, working alongside gracious mortal partners to create works of subtle design and powerful magical potential. What started as a collaboration with mortals soon morphed into abuse, disrespect, and even slavery and bondage. Eventually, these genies rebelled, but in doing so, they came under the sway of a nihilistic demigod known as Ahriman. Their new master twisted their form and granted them the power to avenge themselves upon their mortal overlords, leading to the birth of the first divs.

Since that first wave of corruption, new divs arise from the spirits of the most wicked and hateful genies who die on the Material Plane, or those truly betrayed by mortals and overcome through their desire for vengeance. Upon such a death, instead of returning to the Elemental Planes, these genies' spirits are trapped in the dread orbit of Abaddon, where Ahriman reshapes them as divs and hoists them back to the world to wreak vengeance upon mortals.

```statblock
creature: "Sepid"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
