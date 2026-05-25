---
type: creature
group: ["Div", "Fiend"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Aghash"
level: "4"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Medium"
trait_01: "Div"
trait_02: "Fiend"
trait_03: "Unholy"
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+12; [[Greater Darkvision]]"
languages: "Common, Daemonic (telepathy 100 feet)"
skills:
  - name: Skills
    desc: "Arcana +9, Athletics +8, Deception +12, Intimidation +12, Religion +10, Stealth +10"
abilityMods: ["+3", "+4", "+3", "+1", "+2", "+4"]
abilities_top:
  - name: "Telepathy 100 feet"
    desc: "A monster with telepathy can communicate mentally with any creatures within the listed radius, as long as they share a language. This doesn't give any special access to their thoughts, and communicates no more information than normal speech would."
armorclass:
  - name: AC
    desc: "19; **Fort** +9, **Ref** +10, **Will** +12"
health:
  - name: HP
    desc: "75; **Immunities** curse; **Weaknesses** cold iron 5, holy 5"
abilities_mid:
  - name: "+1 Status to All Saves vs. Magic"
    desc: ""
  - name: "Hatred of Beauty"
    desc: "While aghashes hate all mortals, they particularly despise beautiful objects and beautiful or charismatic mortals. When not in physical peril, an aghash is compelled to destroy art and other works of beauty. An aghash can't enter an area of pristine beauty without first marring it in some way. <br>  <br> Given a choice, an aghash attacks a foe with the highest Charisma score first. If barred from doing so by force or some magical effect, they take 1d6 mental damage at the end of their turn."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Claw +14 (`pf2:1`) (agile, finesse, magical, unarmed, unholy), **Damage** 2d6+5 slashing"
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 21, attack +13<br>**4th** [[Outcast's Curse]], [[Translocate]]<br>**2nd** [[Stupefy]] (At Will)<br>**1st** [[Detect Magic]], [[Illusory Object]] (At Will)"
abilities_bot:
  - name: "Cursed Gaze"
    desc: "`pf2:2` The aghash fixes their gaze on one creature they can see within 20 feet. The creature must attempt a DC 21 [[Will]] save. <br> - **Critical Success** The creature is unaffected. <br> - **Success** The creature takes 2d6 mental damage and becomes [[Frightened]] 1. <br> - **Failure** The creature takes 4d6 mental damage and becomes either [[Frightened]] 2 or [[Stunned]] 1 (the aghash's choice). <br> - **Critical Failure** The creature takes 8d6 mental damage and becomes [[Frightened]] 2 and [[Stunned]] 2."
  - name: "Sandstorm"
    desc: "`pf2:3` **Frequency** once per day <br>  <br> **Effect** The aghash creates a temporary sandstorm in a @Template[emanation|distance:30] that lasts for 1 minute. <br>  <br> Creatures within the emanation take a –4 circumstance penalty to Perception checks and must succeed at a DC 18 [[Fortitude]] save. On a failure, they're forced to hold their breath or else they start suffocating. A creature within the sandstorm at the end of its turn takes @Damage[1d6[slashing]|options:area-damage] damage. <br>  <br> Divs are immune to all effects of an aghash's sandstorm. <br>  <br> > [!danger] Effect: Sandstorm"
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

Walking embodiments of curses, misfortune, and the evil eye, aghashes wander the deserts of the Material Plane, searching out the arrogant, charming, and persuasive to humiliate and undermine. Aghashes are often mistaken for some strange form of hag, and like those creatures, they're masters at curses.

Some fiends want to tear down the multiverse; others dedicate themselves to creating chaos and carnage, or to rule over realms with an iron fist. Divs strive toward a different, if equally reprehensible, goal-they seek to thwart and ruin the schemes and works of mortal beings.

Long ago, divs were once genies bound to serve ancient mortal empires lost to the passage of eons. In the beginning, these genies were masters of creation, working alongside gracious mortal partners to create works of subtle design and powerful magical potential. What started as a collaboration with mortals soon morphed into abuse, disrespect, and even slavery and bondage. Eventually, these genies rebelled, but in doing so, they came under the sway of a nihilistic demigod known as Ahriman. Their new master twisted their form and granted them the power to avenge themselves upon their mortal overlords, leading to the birth of the first divs.

Since that first wave of corruption, new divs arise from the spirits of the most wicked and hateful genies who die on the Material Plane, or those truly betrayed by mortals and overcome through their desire for vengeance. Upon such a death, instead of returning to the Elemental Planes, these genies' spirits are trapped in the dread orbit of Abaddon, where Ahriman reshapes them as divs and hoists them back to the world to wreak vengeance upon mortals.

```statblock
creature: "Aghash"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
