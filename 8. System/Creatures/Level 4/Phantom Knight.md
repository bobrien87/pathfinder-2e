---
type: creature
group: ["Ethereal", "Incorporeal"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Phantom Knight"
level: "4"
rare_01: "Uncommon"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Medium"
trait_01: "Ethereal"
trait_02: "Incorporeal"
trait_03: "Phantom"
trait_04: "Spirit"
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+13; [[Darkvision]]"
languages: "Common"
skills:
  - name: Skills
    desc: "Intimidation +12"
abilityMods: ["-5", "+4", "+0", "+0", "+5", "+4"]
abilities_top:
  - name: "Phantom Touch"
    desc: "Each time they make a Strike, a phantom can choose to deal spirit damage instead of the normal physical damage type."
armorclass:
  - name: AC
    desc: "21; **Fort** +8, **Ref** +12, **Will** +13"
health:
  - name: HP
    desc: "45; **Immunities** disease, paralyzed, poison, precision, bleed; **Resistances** all damage 3 except force, ghost touch, spirit"
abilities_mid:
  - name: "-1 Status to All Saves vs. Death Effects"
    desc: ""
  - name: "Susceptible to Death"
    desc: "Though phantoms aren't alive, neither are they undead, and they are uniquely vulnerable to the effects of death. <br>  <br> A phantom whose Hit Points are reduced to 0 as a result of a death effect (such as from a spell like [[Execute]]) is immediately whisked away to the River of Souls, where their soul resumes the usual path to the afterlife."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Phantom Sword +14 (`pf2:1`) (finesse, magical, versatile p), **Damage** 1d8+7 slashing"
  - name: "Ranged strike"
    desc: "Phantom Bow +14 (`pf2:1`) (deadly d10, magical, volley 30, range 120 ft.), **Damage** 1d8+5 piercing"
spellcasting: []
abilities_bot:
  - name: "Walk the Ethereal Line"
    desc: "`pf2:2` The phantom walks the thin line between the Ethereal Plane and the Universe in order to exist on both planes simultaneously. <br>  <br> They can shift back to solely the Ethereal Plane by using this ability again."
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

Cavaliers and knights who died for their cause make for particularly strongwilled phantoms. Though their motives vary, these phantoms often seek to continue their lifelong missions even in their purgatorial states, and their strong forces of will make them formidable fighters in spite of their incorporeality. A phantom knight might strive to find living followers of their church or order, or seek out other mortals they knew in life as a way of staying grounded and avoiding the corruption of undeath.

The typical trajectory for souls passing to the afterlife is fairly straightforward, according to most theologians. When a mortal dies, their soul enters the River of Souls and eventually reaches the Boneyard, where it is judged by Pharasma. The judged soul moves onto its appropriate domain of final rest—Heaven, Hell, Abaddon, and so forth—where it becomes a shade.

Complications arise, however, when a soul in queue for judgment prematurely departs from the River of Souls and is shunted into the Ethereal Plane. Whether as a result of nefarious interlopers like daemons or hags, malignant planar magic, or even fate, these souls become dislodged from the natural order of life and death and linger in a sort of purgatory. Unlike petitioners, these ethereal phantoms retain memories of their life before death, and unlike spirits such as ghosts, phantoms aren't tinged with the foul influences of undeath—at least, not at first, though the threat of corruption hangs heavy over a phantom's existence. Some eventually succumb to that fate, while others eventually rejoin the River of Souls. Until then, these wandering souls are a kind unto themselves—one without a true home, agenda, or purpose.

Many phantoms have no desire to remain in their strange state of purgatory, either because they seek to continue their journey through the River of Souls or because they fear the corruption of undeath. In order to complete the natural spiritual cycle and become judged so they can continue to the afterlife, a phantom must find a way back into the River of Souls. Such a quest is no easy feat, however—the hazy mists of the Ethereal Plane can befuddle even the most experienced traveler, and numerous predators prowl the realm in search of stray souls to bind or devour.

```statblock
creature: "Phantom Knight"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
