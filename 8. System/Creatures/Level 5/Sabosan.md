---
type: creature
group: ["Humanoid"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Sabosan"
level: "5"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Medium"
trait_01: "Humanoid"
trait_02: ""
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+10; [[Echolocation]] (precise) 20 feet, [[Low-Light Vision]], [[Scent]] (imprecise) 30 feet"
languages: "Chthonian, Mwangi"
skills:
  - name: Skills
    desc: "Acrobatics +13, Athletics +12, Stealth +13"
abilityMods: ["+4", "+5", "+2", "-1", "+1", "+0"]
abilities_top:
  - name: "Echolocation 20 feet"
    desc: "A sabosan can use their hearing as a precise sense at the listed range."
armorclass:
  - name: AC
    desc: "22; **Fort** +11, **Ref** +14, **Will** +10"
health:
  - name: HP
    desc: "78"
abilities_mid: []
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Jaws +15 (`pf2:1`) (finesse, unarmed), **Damage** 2d10+4 piercing plus 1 bleed"
  - name: "Melee strike"
    desc: "Claw +15 (`pf2:1`) (agile, finesse, unarmed), **Damage** 2d8+4 slashing plus [[Grab]]"
  - name: "Melee strike"
    desc: "Spear +14 (`pf2:1`), **Damage** 1d6+7 piercing"
  - name: "Melee strike"
    desc: "Spear +15 (`pf2:1`) (thrown 20), **Damage** 1d6+7 piercing"
spellcasting: []
abilities_bot:
  - name: "Drain Blood"
    desc: "`pf2:1` **Requirements** The sabosan has a creature [[Grabbed]] or [[Restrained]] <br>  <br> **Effect** The sabosan drains blood from the creature. The creature must succeed at a DC 22 [[Fortitude]] save or become [[Drained]] 1. The sabosan gains a number of temporary Hit Points equal to the number of Hit Points lost by the creature due to its drained condition."
  - name: "Fell Shriek"
    desc: "`pf2:2` The sabosan emits a deafening cry in a @Template[type:cone|distance:30]. Non-sabosan creatures in this area must each succeed at a DC 22 [[Fortitude]] save or be [[Deafened]] for 1 minute."
  - name: "Powerful Charge"
    desc: "`pf2:2` The sabosan Strides or Flies up to double their Speed and then makes a claw Strike. If the sabosan moved at least 20 feet, they deal an additional 1d6 slashing damage on a hit."
  - name: "Grab"
    desc: "`pf2:1` **Requirements** The monster's last action was a successful Strike that lists Grab in its damage entry, or the monster has a creature [[Grabbed]] or [[Restrained]] <br>  <br> **Effect** If used after a Strike, the monster attempts to `act grapple` the creature using the body part it attacked with. This attempt neither applies nor counts toward the creature's multiple attack penalty. <br>  <br> The monster can instead use Grab and choose one creature it's grabbing or restraining with an appendage that has Grab to automatically extend that condition to the end of the monster's next turn."
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

Sabosans are intelligent, bat-like humanoids who live in warm forests and drink the blood of other creatures, particularly people. They have thin, emaciated torsos and broad, leathery wings that can reach a span of almost 20 feet. Sabosans' heads, necks, shoulders, and upper chests are covered with red or dark-brown fur that obscures their stretched-thin flesh. Though their ears are large and pointed like a bat's and they can echolocate as bats do, their vision is also quite strong, enough so that they can use it to easily track quarry in low light.

Some naturalist scholars believe that sabosans are distant descendants of humans who were afflicted with vampirism but managed to avoid succumbing to undeath. Others posit they were once a cult of demon worshippers whose dark rites transformed them into their current forms. No matter their true origins, sabosans have infamous reputations among towns and cities south of Golarion's equator. Even mere rumors of sabosans in an area are enough to set off city-wide hunts, and the truly superstitious aren't above setting fires near every grotto, nook, and foxhole they come across in order to smoke out the nocturnal creatures.

Sabosans hunt during the twilight hours or just after dark, when their echolocation gives them an edge over sleeping prey. They are capable hunters but indiscriminating when it comes to food sources; their rapid metabolisms means sabosans must eat nearly 20 pounds of meat and fruit per day, supplemented, of course, with copious amounts of blood.

Sabosans' obscure faith reveres two deities: the slain Demon Lord Vyriavaxus, Lord of Shadows, and the nearly forgotten sun god Easivra. Vyriavaxus has an obvious link with the creatures, with his appearance as a giant bat, but their connection to the sun god hints at a complex depth in sabosan beliefs.

```statblock
creature: "Sabosan"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
